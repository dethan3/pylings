import importlib.util
import sys
import os

def test_lists1():
    file_path = os.path.abspath("exercises/04_lists/lists1.py")
    spec = importlib.util.spec_from_file_location("lists1", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    fruits = vars.get("fruits")
    assert isinstance(fruits, list), "fruits should be a list"
    assert fruits == ["apple", "banana", "cherry"], "fruits list content is incorrect"
    
    assert vars.get("first_fruit") == "apple", "first_fruit should be 'apple'"
    assert vars.get("last_fruit") == "cherry", "last_fruit should be 'cherry'"
