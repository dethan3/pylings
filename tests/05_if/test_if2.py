import importlib.util
import sys
import os

def test_if2():
    file_path = os.path.abspath("exercises/05_if/if2.py")
    spec = importlib.util.spec_from_file_location("if2", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    assert module.practice(10) == "Child", "10 should be 'Child'"
    assert module.practice(13) == "Teenager", "13 should be 'Teenager'"
    assert module.practice(19) == "Teenager", "19 should be 'Teenager'"
    assert module.practice(20) == "Adult", "20 should be 'Adult'"
