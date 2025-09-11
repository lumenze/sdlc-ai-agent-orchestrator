import csv
from io import StringIO
from fastapi.responses import StreamingResponse
from src.utils.logger import logger

def extract_csv_code_block(markdown: str) -> str:
    """Extracts a ```csv ... ``` code block from markdown text."""
    in_block = False
    csv_lines = []
    for line in markdown.splitlines():
        if line.strip().startswith("```csv"):
            in_block = True
            continue
        if in_block and line.strip().startswith("```"):
            break
        if in_block:
            csv_lines.append(line.strip())
    return "\n".join(csv_lines)

def convert_markdown_to_csv(markdown_str: str) -> StreamingResponse:
    logger.info("🔁 Converting markdown to CSV stream")
    csv_str = extract_csv_code_block(markdown_str)

    if not csv_str.strip():
        raise ValueError("No CSV block found in markdown.")

    csv_buffer = StringIO(csv_str)
    reader = csv.DictReader(csv_buffer)

    if not reader.fieldnames:
        raise ValueError("No fieldnames detected in CSV block.")

    cleaned_rows = []
    for i, row in enumerate(reader):
        if None in row:
            logger.warning(f"⚠️ Skipping malformed row {i + 1}: {row}")
            continue
        cleaned_rows.append(row)

    if not cleaned_rows:
        raise ValueError("No valid rows to write in CSV.")

    # Reset buffer for writing
    out_buffer = StringIO()
    writer = csv.DictWriter(out_buffer, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_rows)
    out_buffer.seek(0)

    logger.info("✅ CSV streaming response ready")
    return StreamingResponse(
        out_buffer,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=jira_tickets.csv"}
    )