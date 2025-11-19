import importlib.util
import sys
import os
import inspect

def test_classes1():
    file_path = os.path.abspath("exercises/09_classes/classes1.py")
    spec = importlib.util.spec_from_file_location("classes1", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    vars = module.practice()
    
    assert "Dog" in vars, "Class 'Dog' is not defined"
    Dog = vars["Dog"]
    assert inspect.isclass(Dog), "'Dog' should be a class"
    
    my_dog = vars.get("my_dog")
    assert isinstance(my_dog, Dog), "'my_dog' should be an instance of Dog"
    assert my_dog.name == "Fido", "The dog's name should be 'Fido'"
    assert my_dog.bark() == "Woof!", "The dog should bark 'Woof!'"
