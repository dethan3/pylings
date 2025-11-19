import importlib.util
import sys
import os

def test_loops2():
    file_path = os.path.abspath("exercises/06_loops/loops2.py")
    spec = importlib.util.spec_from_file_location("loops2", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    assert vars.get("counter") == 5, "Counter should be 5 after the loop"
