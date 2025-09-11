# tests/test_ticket_generation_service.py

import pytest
from fastapi import HTTPException
from fastapi.responses import StreamingResponse
from unittest.mock import patch
from io import StringIO

from src.services.ticket_generation_service import process_ticket_generation

@pytest.fixture
def mock_input_text():
    return "# Sample Requirement\n\n## Story\n- Build login system"

@patch("src.services.ticket_generation_service.save_response_to_cache")
@patch("src.services.ticket_generation_service.get_cache_key")
@patch("src.services.ticket_generation_service.get_cached_response")
@patch("src.services.ticket_generation_service.generate_jira_tickets_from_requirements")
def test_process_ticket_generation_success(
    mock_generate_jira,
    mock_get_cached,
    mock_get_key,
    mock_save_cache,
    mock_input_text,
):
    mock_get_key.return_value = "mock_key"
    mock_get_cached.return_value = None
    mock_generate_jira.return_value = (
        "```csv\nTicket ID,Summary,Issue Type,Description,Acceptance Criteria,Priority,Labels,Story Points,Component,Parent ID\n"
        "PROJ-101,Sample Ticket,Epic,Description,Criteria,High,auth,3,core,\n```"
    )

    response = process_ticket_generation(mock_input_text)
    assert isinstance(response, StreamingResponse)
    assert response.status_code == 200 or response.status_code is None  # StreamingResponse returns no code by default

@patch("src.services.ticket_generation_service.get_cache_key")
@patch("src.services.ticket_generation_service.get_cached_response")
def test_process_ticket_generation_uses_cache(mock_get_cached, mock_get_key, mock_input_text):
    mock_get_key.return_value = "mock_key"
    mock_get_cached.return_value = (
        "```csv\nTicket ID,Summary,Issue Type,Description,Acceptance Criteria,Priority,Labels,Story Points,Component,Parent ID\n"
        "PROJ-101,Cached Ticket,Epic,Description,Criteria,High,auth,3,core,\n```"
    )

    response = process_ticket_generation(mock_input_text)
    assert isinstance(response, StreamingResponse)

@patch("src.services.ticket_generation_service.get_cache_key")
@patch("src.services.ticket_generation_service.get_cached_response")
@patch("src.services.ticket_generation_service.generate_jira_tickets_from_requirements")
def test_process_ticket_generation_llm_failure(mock_generate_jira, mock_get_cached, mock_get_key, mock_input_text):
    mock_get_key.return_value = "mock_key"
    mock_get_cached.return_value = None
    mock_generate_jira.return_value = ""

    with pytest.raises(HTTPException) as exc_info:
        process_ticket_generation(mock_input_text)

    assert exc_info.value.status_code == 500
    assert "LLM generation returned empty output" in str(exc_info.value.detail)