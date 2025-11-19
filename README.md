# 🐍 Pylings - Interactive Python Learning

Welcome to **Pylings**! This project is designed to help you learn Python through interactive exercises, similar to the famous Rustlings project.

> 🎯 **Goal**: Learn Python by fixing broken code and passing tests.
> 🧠 **Philosophy**: Learn by Doing. Small, focused exercises with immediate feedback.

## 🚀 Quick Start

### 1. Setup

You can set up the environment automatically using the provided script:

```bash
./setup.sh
```

### 2. Start Learning

Activate the virtual environment and start the interactive runner:

```bash
source .venv/bin/activate
python3 pylings.py watch
```

The runner will:
1.  Run the current exercise.
2.  Show you the error output if it fails.
3.  Wait for you to fix the code.
4.  Automatically move to the next exercise when you pass!

## 📁 Project Structure

```
python-learning/
├── exercises/           # ✍️ Your Code Goes Here!
│   ├── 01_variables/    # Variables
│   ├── 02_strings/      # Strings
│   ├── 03_numbers/      # Numbers
│   ├── 04_lists/        # Lists
│   ├── 05_if/           # Control Flow
│   ├── 06_loops/        # Loops
│   ├── 07_functions/    # Functions
│   ├── 08_dictionaries/ # Dictionaries
│   ├── 09_classes/      # Classes & OOP
│   ├── 10_exceptions/   # Error Handling
│   ├── 11_files/        # File I/O
│   └── projects/        # Larger projects
├── tests/               # 🧪 Automated Tests (Don't peek unless stuck!)
├── pylings.py           # 🏃 The CLI Runner
└── setup.sh             # 🛠️ Setup Script
```

## 📝 How to Solve Exercises

1.  **Read the Error**: The runner output will tell you what went wrong.
2.  **Open the File**: Go to the file path shown in the runner (e.g., `exercises/01_variables/variables1.py`).
3.  **Fix the Code**: Follow the instructions in the comments (look for `TODO`).
4.  **Remove the Marker**: Delete the line `# I AM NOT DONE` when you think you've solved it.
5.  **Save**: The runner will automatically check your solution.

## 🤝 Contributing

Feel free to add more exercises or improve existing ones! Check `exercises/info.toml` to see how exercises are registered.

---
**Happy Coding!** 🐍

## License

MIT