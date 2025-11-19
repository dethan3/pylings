import importlib.util
import sys
import os

def test_dicts1():
    file_path = os.path.abspath("exercises/08_dictionaries/dicts1.py")
    spec = importlib.util.spec_from_file_location("dicts1", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    person = vars.get("person")
    assert isinstance(person, dict), "person should be a dictionary"
    assert person.get("name") == "Alice", "person['name'] should be 'Alice'"
    assert person.get("age") == 30, "person['age'] should be 30"
    
    assert vars.get("name") == "Alice", "Variable 'name' should be 'Alice'"
    assert vars.get("age") == 30, "Variable 'age' should be 30"
