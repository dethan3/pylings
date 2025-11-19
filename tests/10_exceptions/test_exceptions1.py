import importlib.util
import sys
import os

def test_exceptions1():
    file_path = os.path.abspath("exercises/10_exceptions/exceptions1.py")
    spec = importlib.util.spec_from_file_location("exceptions1", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    assert module.practice("123") == 123, "Should convert '123' to 123"
    assert module.practice("abc") == -1, "Should return -1 for invalid input 'abc'"
