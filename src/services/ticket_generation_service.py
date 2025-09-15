from fastapi import HTTPException
from fastapi.responses import StreamingResponse
from src.core.llm_client import generate_jira_tickets_from_requirements
from src.utils.logger import logger
from src.utils.cache import get_cache_key, get_cached_response, save_response_to_cache
from io import StringIO

def process_ticket_generation(content_str: str) -> StreamingResponse:
    try:
        # Step 1: Check cache
        cache_key = get_cache_key(content_str)
        cached_output = get_cached_response(cache_key)
        if cached_output:
            logger.info("✅ Using cached GPT output")
            csv_output = cached_output
        else:
            logger.info("🚀 Generating Jira CSV using LLM")
            csv_output = generate_jira_tickets_from_requirements(content_str)
            logger.info("🧠 GPT raw output:\n" + csv_output[:1000])
            if not csv_output:
                raise ValueError("LLM generation returned empty output")
            save_response_to_cache(cache_key, csv_output)
            logger.info("✅ LLM output cached")

        # Step 2: Clean up the GPT CSV output (remove ```csv blocks if present)
        if csv_output.startswith("```csv"):
            csv_output = csv_output.strip("```csv").strip("```").strip()
        elif csv_output.startswith("```"):
            csv_output = csv_output.strip("```").strip()

        # Step 3: Stream the CSV directly
        csv_buffer = StringIO(csv_output)
        logger.info("✅ CSV streaming response ready")

        return StreamingResponse(
            csv_buffer,
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=jira_tickets.csv"}
        )

    except ValueError as ve:
        logger.error(f"❌ LLM Generation Error: {ve}")
        raise HTTPException(status_code=500, detail=str(ve))

    except Exception as e:
        logger.exception("❌ Unexpected error during ticket generation")
        raise HTTPException(status_code=500, detail="Internal Server Error during ticket generation")