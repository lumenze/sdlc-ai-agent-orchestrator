# tests/test_logger.py

import logging
import os
from src.utils.logger import logger

def test_logger_is_instance_of_logging_logger():
    """Ensure logger is properly configured."""
    assert isinstance(logger, logging.Logger)
    assert logger.name == "sdlc_ai_agent"

def test_logger_outputs_to_file(tmp_path):
    """Verify logger writes expected output to file."""
    test_log_path = tmp_path / "test_app.log"

    # Set up a custom file handler for testing
    test_handler = logging.FileHandler(test_log_path)
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
    test_handler.setFormatter(formatter)

    logger.addHandler(test_handler)
    logger.setLevel(logging.INFO)

    # Write test message
    test_message = "🚀 Logger is working as expected!"
    logger.info(test_message)

    # Remove the test handler
    logger.removeHandler(test_handler)

    # Check contents of the log file
    with open(test_log_path, "r", encoding="utf-8") as f:
        log_contents = f.read()

    assert test_message in log_contents
    assert "INFO" in log_contents
    assert "sdlc_ai_agent" in log_contents