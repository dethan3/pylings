import importlib.util
import sys
import os
import inspect

def test_classes2():
    file_path = os.path.abspath("exercises/09_classes/classes2.py")
    spec = importlib.util.spec_from_file_location("classes2", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    assert "Cat" in vars, "Class 'Cat' is not defined"
    Cat = vars["Cat"]
    Animal = vars["Animal"]
    
    assert issubclass(Cat, Animal), "'Cat' should inherit from 'Animal'"
    
    my_cat = vars.get("my_cat")
    assert isinstance(my_cat, Cat), "'my_cat' should be an instance of Cat"
    assert my_cat.speak() == "Meow", "The cat should say 'Meow'"
