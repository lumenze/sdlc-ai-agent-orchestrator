import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage
from src.utils.logger import logger

# Set model to GPT-4o for now
MODEL = "gpt-4o"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_jira_tickets_from_requirements(requirements_text: str) -> str:
    """
    Generate JIRA ticket markdown from the given requirements using OpenAI's LLM.

    Args:
        requirements_text (str): Raw requirements input from user.

    Returns:
        str: Markdown-formatted string representing epics, stories, and tasks with metadata.
    """
    try:
        logger.info("🚀 Sending prompt to GPT model...")

        messages = [
            {
                "role": "system",
                "content": (
                                """You are a senior software delivery assistant. Your job is to convert a business requirements document 
                            into a flat CSV table suitable for importing into JIRA. For each Epic, Story, and Task, include the following fields:

                            - Ticket ID (use format PROJ-101, PROJ-102, etc.)
                            - Summary
                            - Issue Type (Epic, Story, Task)
                            - Description (user stories should use the format: As a ___, I want ___ so that ___)
                            - Acceptance Criteria (write clear conditions of satisfaction)
                            - Priority (High, Medium, Low)
                            - Labels (comma-separated)
                            - Story Points (optional for epics)
                            - Component (e.g., authentication, dashboard, etc.)
                            - Parent ID (leave blank for Epics, fill in Epic/Story ID for Stories and Tasks)

                            Return **only** the CSV content, with headers, wrapped in a markdown CSV block like:
                            ```csv
                            ...csv here...
                            ```"""
        )
            },
            {
                "role": "user",
                "content": requirements_text,
            },
        ]

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.2,
            max_tokens=4096,
        )

        markdown_output = response.choices[0].message.content.strip()
        logger.info("✅ Successfully received markdown output from GPT.")

        return markdown_output

    except Exception as oe:
        logger.error(f"🛑 OpenAI API error: {oe}")
        raise

    except Exception as e:
        logger.exception("❌ Unexpected error while generating tickets")
        raise
