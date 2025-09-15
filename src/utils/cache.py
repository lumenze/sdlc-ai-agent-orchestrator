import hashlib
import os
import redis
from src.utils.logger import logger

TTL_SECONDS = 60 * 60 * 24  # 1 day

# Setup Redis once (lazy)
redis_client = None
try:
    redis_client = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        decode_responses=True
    )
except Exception as e:
    logger.error(f"❌ Redis connection failed: {e}")
    redis_client = None

def get_cache_key(content: str) -> str:
    """Generate a consistent cache key from markdown content."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

def get_cached_response(key: str) -> str | None:
    """Retrieve cached GPT output if exists."""
    cache_dir = os.getenv("CACHE_DIR")
    if cache_dir:
        try:
            cache_file_path = os.path.join(cache_dir, key)
            if os.path.exists(cache_file_path):
                with open(cache_file_path, "r", encoding="utf-8") as f:
                    return f.read()
        except Exception as e:
            logger.warning(f"⚠️ File cache read failed for key {key}: {e}")
        return None

    elif redis_client:
        try:
            return redis_client.get(key)
        except Exception as e:
            logger.warning(f"⚠️ Redis get failed for key {key}: {e}")
    return None

def save_response_to_cache(key: str, value: str) -> None:
    """Save GPT output to cache for future reuse."""
    cache_dir = os.getenv("CACHE_DIR")
    if cache_dir:
        try:
            os.makedirs(cache_dir, exist_ok=True)
            cache_file_path = os.path.join(cache_dir, key)
            with open(cache_file_path, "w", encoding="utf-8") as f:
                f.write(value)
            logger.info(f"💾 File cache saved for key {key}")
        except Exception as e:
            logger.warning(f"⚠️ File cache write failed for key {key}: {e}")
        return

    elif redis_client:
        try:
            redis_client.setex(key, TTL_SECONDS, value)
            logger.info(f"💾 Redis cache saved for key {key}")
        except Exception as e:
            logger.warning(f"⚠️ Redis set failed for key {key}: {e}")