import importlib.util
import sys
import os

def test_numbers1():
    file_path = os.path.abspath("exercises/03_numbers/numbers1.py")
    spec = importlib.util.spec_from_file_location("numbers1", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    assert vars.get("sum") == 15, "5 + 10 should be 15"
    assert vars.get("difference") == 95, "100 - 5 should be 95"
    assert vars.get("product") == 42, "6 * 7 should be 42"
    assert vars.get("quotient") == 10.0, "80 / 8 should be 10.0"
