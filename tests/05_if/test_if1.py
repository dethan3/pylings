import importlib.util
import sys
import os

def test_if1():
    file_path = os.path.abspath("exercises/05_if/if1.py")
    spec = importlib.util.spec_from_file_location("if1", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    assert module.practice(20) == "Big", "20 is greater than 10, should return 'Big'"
    assert module.practice(5) == "Small", "5 is not greater than 10, should return 'Small'"
    assert module.practice(10) == "Small", "10 is not greater than 10, should return 'Small'"
