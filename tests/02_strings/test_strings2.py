import importlib.util
import sys
import os

def test_strings2():
    file_path = os.path.abspath("exercises/02_strings/strings2.py")
    spec = importlib.util.spec_from_file_location("strings2", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    assert vars.get("message") == "I am learning Python version 3.11", "The message is incorrect. Did you use f-string?"
