import importlib.util
import sys
import os

def test_dicts2():
    file_path = os.path.abspath("exercises/08_dictionaries/dicts2.py")
    spec = importlib.util.spec_from_file_location("dicts2", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    car = vars.get("car")
    assert car.get("year") == 2020, "Year should be updated to 2020"
    assert car.get("color") == "red", "Key 'color' should be added with value 'red'"
    assert "model" not in car, "Key 'model' should be removed"
