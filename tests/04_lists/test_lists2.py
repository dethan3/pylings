import importlib.util
import sys
import os

def test_lists2():
    file_path = os.path.abspath("exercises/04_lists/lists2.py")
    spec = importlib.util.spec_from_file_location("lists2", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    numbers = vars.get("numbers")
    assert 6 in numbers, "Number 6 should be appended to the list"
    assert 3 not in numbers, "Number 3 should be removed from the list"
    assert numbers == [1, 2, 4, 5, 6], "Final list should be [1, 2, 4, 5, 6]"
