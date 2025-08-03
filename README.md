# To-Do CLI App

This is a simple command-line interface (CLI) application for managing a to-do list. You can add tasks, list all tasks, and mark tasks as done.

---

## ✨ Features

- Add tasks to your to-do list
- List all tasks with their status (done or not done)
- Mark tasks as done
- View task statistics (total, completed, pending)

---

## 📦 Requirements

- Python 3.11 or higher  
- [`coverage`](https://pypi.org/project/coverage/) package (for testing and coverage reports)

---

## 🚀 Usage

Run the application using the `main.py` script.

### ➕ Add a Task

```bash
python -m todo_cli.main add "Task description"
```

**Example:**

```bash
python -m todo_cli.main add "Buy groceries"
```

---

### 📋 List Tasks

```bash
python -m todo_cli.main list
```

**Example output:**

```
Your to-do list:
1. [❌] Buy groceries  
2. [✔️] Complete homework
3. [❌] Walk the dog
```

---

### ✅ Mark a Task as Done

```bash
python -m todo_cli.main done INDEX
```

**Example:**

```bash
python -m todo_cli.main done 1
```

This will mark the first task as done.

---

### 📊 View Statistics

```bash
python -m todo_cli.main stats
```

**Example output:**

```
Task Statistics:
  Total tasks: 3
  Completed: 2
  Pending: 1
```

---

## 🧪 Running Tests

To run unit tests and generate a coverage report:

```bash
coverage run -m unittest discover tests
coverage report
```

Current test coverage: **99%**

---

## 📁 Project Structure

```
todo_cli/
├── __init__.py       # Package initialization
├── main.py           # CLI entry point
└── task_manager.py   # Logic for loading, saving, listing, adding, and marking tasks

tests/
├── __init__.py       # Test package initialization
└── test_task_manager.py   # Unit tests

.github/workflows/
└── sonar.yml         # GitHub Actions workflow for SonarQube

sonar-project.properties  # SonarQube project configuration
```

---

## 📊 SonarQube Integration

This project includes GitHub Actions CI for SonarQube analysis. To enable it, add the following secrets in your GitHub repository:

- `SONAR_TOKEN`: Your SonarQube or SonarCloud authentication token  
- `SONAR_HOST_URL`: The URL of your SonarQube instance (e.g., `https://sonarcloud.io`)

---

## 🏗️ Architecture

The application follows a clean, modular architecture:

### Core Components

1. **TaskManager** (`task_manager.py`): Handles all task operations
   - Loading/saving tasks from JSON storage
   - Adding new tasks with validation
   - Marking tasks as complete
   - Generating task statistics

2. **CLI Interface** (`main.py`): Command-line interface
   - Argument parsing using `argparse`
   - Command routing and error handling
   - User-friendly help and examples

3. **Data Storage**: JSON-based persistence
   - Human-readable format
   - Automatic file creation
   - Error handling for corrupted files

### Data Flow

1. User runs command → CLI parses arguments
2. TaskManager loads existing tasks from JSON
3. Command executes and modifies tasks
4. Changes are saved back to JSON file
5. Results displayed to user

---

## 🔧 Technical Details

- **Language**: Python 3.11+
- **Dependencies**: Built-in libraries only (no external dependencies for core functionality)
- **Storage**: JSON files for data persistence
- **Testing**: Comprehensive unit tests with 99% coverage
- **CI/CD**: GitHub Actions with SonarQube integration
- **Code Quality**: Type hints, error handling, and comprehensive documentation

---

## 🚀 Getting Started

1. Clone or download the project
2. Ensure Python 3.11+ is installed
3. Install coverage for testing: `pip install coverage`
4. Run the application: `python -m todo_cli.main --help`
5. Add your first task: `python -m todo_cli.main add "My first task"`
6. List your tasks: `python -m todo_cli.main list`

---

## 📝 License

This project is open source and available under standard terms.