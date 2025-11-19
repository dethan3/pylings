import importlib.util
import sys
import os

def test_loops1():
    file_path = os.path.abspath("exercises/06_loops/loops1.py")
    spec = importlib.util.spec_from_file_location("loops1", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice([1, 2, 3, 4, 5])
    
    assert vars.get("sum") == 15, "Sum of [1, 2, 3, 4, 5] should be 15"
    
    vars2 = module.practice([10, 20, 30])
    assert vars2.get("sum") == 60, "Sum of [10, 20, 30] should be 60"
