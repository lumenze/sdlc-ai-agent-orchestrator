from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from src.services.ticket_generation_service import process_ticket_generation
from src.utils.logger import logger

router = APIRouter()

@router.post("/generate-tickets", response_class=StreamingResponse)
async def generate_tickets(requirements_file: UploadFile = File(...)):
    logger.info("📥 /generate-tickets called")

    try:
        content = await requirements_file.read()
        if not content:
            raise HTTPException(status_code=400, detail="Uploaded file is empty...")

        content_str = content.decode("utf-8")

        # 🔄 In-memory streaming response
        return process_ticket_generation(content_str)

    except HTTPException as he:
        logger.error(f"❌ Error in /generate-tickets route: {he.detail}")
        raise he

    except Exception as e:
        logger.exception("❌ Unexpected error in /generate-tickets route")
        raise HTTPException(status_code=500, detail="Internal server error during ticket generation")