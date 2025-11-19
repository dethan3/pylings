import sys
import time
import toml
import subprocess
import os
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

console = Console()

CONFIG_FILE = "exercises/info.toml"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        console.print(f"[bold red]Configuration file {CONFIG_FILE} not found![/bold red]")
        sys.exit(1)
    return toml.load(CONFIG_FILE)

def get_exercises(config):
    return config.get("exercises", [])

def run_test(exercise):
    path = exercise["path"]
    name = exercise["name"]
    mode = exercise.get("mode", "test")
    
    console.print(f"[bold blue]Running {name}...[/bold blue]")

    # Check if file has "I AM NOT DONE"
    try:
        with open(path, "r") as f:
            content = f.read()
            if "# I AM NOT DONE" in content:
                console.print(f"[yellow]Exercise {name} is not done yet. Remove '# I AM NOT DONE' to check it.[/yellow]")
                return False
    except FileNotFoundError:
        console.print(f"[bold red]File {path} not found![/bold red]")
        return False

    # Determine test path
    # Assumption: tests are in tests/ folder with same structure or mapped
    # For simplicity, let's assume tests/<exercise_dir>/test_<exercise_name>.py
    # But we need a mapping. Let's check if 'test_path' is in config, or infer it.
    
    # Inference strategy:
    # exercises/01_variables/variables1.py -> tests/01_variables/test_variables1.py
    
    exercise_dir = os.path.dirname(path).replace("exercises/", "")
    exercise_filename = os.path.basename(path)
    test_filename = f"test_{exercise_filename}"
    test_path = os.path.join("tests", exercise_dir, test_filename)

    if mode == "project":
        # For projects, we might just run the main file or a specific test
        # For now, let's assume there is a test file for projects too
        pass

    if not os.path.exists(test_path):
        # Fallback: maybe the test is defined in the config?
        if "test_path" in exercise:
            test_path = exercise["test_path"]
        else:
            console.print(f"[bold red]Test file {test_path} not found for {name}![/bold red]")
            return False

    result = subprocess.run(["pytest", test_path, "-q", "--tb=short"], capture_output=True, text=True)
    
    if result.returncode == 0:
        console.print(f"[bold green]✅ {name} passed![/bold green]")
        return True
    else:
        console.print(f"[bold red]❌ {name} failed![/bold red]")
        console.print(result.stdout)
        console.print(result.stderr)
        return False

def watch_exercises():
    config = load_config()
    exercises = get_exercises(config)
    
    # Find the first failed or pending exercise
    for exercise in exercises:
        if not run_test(exercise):
            console.print(f"\n[bold cyan]Waiting for changes in {exercise['path']}...[/bold cyan]")
            # Simple loop for now, or use watchdog
            # For this implementation, let's just run the check once. 
            # Real "watch" mode would need a loop.
            return

def list_exercises():
    config = load_config()
    exercises = get_exercises(config)
    for ex in exercises:
        console.print(f"- {ex['name']} ({ex['path']})")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "list":
            list_exercises()
        elif cmd == "verify":
            watch_exercises() # Just runs once for now
        elif cmd == "watch":
            # TODO: Implement continuous watching
            watch_exercises()
    else:
        watch_exercises()
