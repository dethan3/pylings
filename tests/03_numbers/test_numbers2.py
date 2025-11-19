import importlib.util
import sys
import os

def test_numbers2():
    file_path = os.path.abspath("exercises/03_numbers/numbers2.py")
    spec = importlib.util.spec_from_file_location("numbers2", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    assert vars.get("my_int") == 123, "String '123' converted to int should be 123"
    assert isinstance(vars.get("my_int"), int), "my_int should be of type int"
    
    assert vars.get("my_str") == "456", "Integer 456 converted to string should be '456'"
    assert isinstance(vars.get("my_str"), str), "my_str should be of type str"
    
    assert vars.get("pi_int") == 3, "Float 3.14 converted to int should be 3"
