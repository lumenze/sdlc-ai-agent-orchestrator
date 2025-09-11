import logging

logger = logging.getLogger("sdlc_ai_agent")
logger.setLevel(logging.INFO)

# Avoid adding multiple handlers if logger is re-imported
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)