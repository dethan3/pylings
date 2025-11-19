import importlib.util
import sys
import os

def test_files1():
    file_path = os.path.abspath("exercises/11_files/files1.py")
    spec = importlib.util.spec_from_file_location("files1", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Ensure clean state
    if os.path.exists("my_file.txt"):
        os.remove("my_file.txt")
        
    vars = module.practice()
    
    assert os.path.exists("my_file.txt"), "File 'my_file.txt' should be created"
    
    with open("my_file.txt", "r") as f:
        content = f.read()
        assert content == "Hello, File!", "File content should be 'Hello, File!'"
        
    assert vars.get("content") == "Hello, File!", "Variable 'content' should contain the file content"
    
    # Cleanup
    if os.path.exists("my_file.txt"):
        os.remove("my_file.txt")
