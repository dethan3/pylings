import importlib.util
import sys
import os

def test_strings1():
    file_path = os.path.abspath("exercises/02_strings/strings1.py")
    spec = importlib.util.spec_from_file_location("strings1", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    assert vars.get("hello") == "Hello", "Variable 'hello' should be 'Hello'"
    assert vars.get("world") == "World", "Variable 'world' should be 'World'"
    assert vars.get("greeting") == "Hello World", "Variable 'greeting' should be 'Hello World'"
