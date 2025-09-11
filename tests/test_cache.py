import hashlib
import os
import shutil
import tempfile
import pytest
from src.utils.cache import get_cache_key, get_cached_response, save_response_to_cache

@pytest.fixture(scope="function")
def temp_cache_dir(monkeypatch):
    # Create a temporary directory for the cache
    temp_dir = tempfile.mkdtemp()
    monkeypatch.setenv("CACHE_DIR", temp_dir)
    yield temp_dir
    shutil.rmtree(temp_dir)

def test_get_cache_key_returns_expected_hash():
    input_str = "This is a test"
    key = get_cache_key(input_str)
    expected = hashlib.sha256(input_str.encode("utf-8")).hexdigest()
    assert key == expected

def test_save_and_get_cached_response(temp_cache_dir, monkeypatch):
    test_key = get_cache_key("sample_input")
    test_content = "Generated markdown from GPT"

    # Save to cache
    save_response_to_cache(test_key, test_content)

    # Retrieve from cache
    result = get_cached_response(test_key)
    assert result == test_content

def test_get_cached_response_returns_none_if_missing(temp_cache_dir):
    fake_key = get_cache_key("this key was never cached")
    result = get_cached_response(fake_key)
    assert result is None