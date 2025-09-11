import pytest
from src.utils.helpers import extract_csv_code_block

def test_extract_csv_block_valid():
    md = """Here is your output:
    ```csv
    col1,col2
    val1,val2
    ```
    """
    expected = "col1,col2\nval1,val2"
    assert extract_csv_code_block(md) == expected

def test_extract_csv_block_no_fence():
    md = """```csv
col1,col2
val1,val2
```"""
    assert extract_csv_code_block(md) == "col1,col2\nval1,val2"

def test_extract_csv_block_wrong_fence():
    md = """```json
{"foo": "bar"}
```"""
    assert extract_csv_code_block(md) == ""