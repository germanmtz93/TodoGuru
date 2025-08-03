# To-Do CLI Application

## Overview

This is a simple command-line interface (CLI) application for managing to-do lists. The application is built in Python and provides comprehensive task management functionality including adding tasks, listing tasks, marking tasks as complete, viewing statistics, and removing tasks. The application uses JSON files for persistent data storage and includes comprehensive testing with 99% code coverage.

## Recent Changes (July 29, 2025)

- ✓ Created comprehensive README.md documentation with usage examples
- ✓ Verified all CLI commands are working correctly (add, list, done, stats)
- ✓ Confirmed test suite passes with 99% coverage
- ✓ Set up workflows for testing the application
- ✓ Validated JSON persistence and error handling

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The application follows a simple modular architecture with clear separation of concerns:

- **CLI Interface Layer**: Handles command-line argument parsing and user interaction
- **Business Logic Layer**: Manages task operations and data validation
- **Data Persistence Layer**: Handles JSON file-based storage

The architecture is lightweight and designed for simplicity, making it easy to understand and extend.

## Key Components

### 1. Task Manager (`task_manager.py`)
- **Purpose**: Core business logic for task operations
- **Responsibilities**: 
  - Loading tasks from JSON storage
  - Saving tasks to JSON storage
  - Managing task data structure
- **Design Decision**: Uses JSON for simplicity and human readability
- **Data Structure**: List of dictionaries with `description` and `done` fields

### 2. Main CLI Interface (`main.py`)
- **Purpose**: Command-line interface and argument parsing
- **Responsibilities**:
  - Parsing command-line arguments using `argparse`
  - Routing commands to appropriate TaskManager methods
  - Providing help and usage information
- **Supported Commands**:
  - `add`: Add new tasks
  - `list`: Display all tasks
  - `done`: Mark tasks as complete
  - `stats`: Show task statistics

### 3. Package Structure
- **`__init__.py`**: Package initialization with version and author information
- **`tests/`**: Unit test suite using Python's unittest framework

## Data Flow

1. **Command Input**: User provides command via CLI arguments
2. **Argument Parsing**: `argparse` processes and validates input
3. **TaskManager Initialization**: Loads existing tasks from JSON file
4. **Command Execution**: Appropriate TaskManager method is called
5. **Data Persistence**: Modified tasks are saved back to JSON file
6. **Output**: Results are displayed to the user

## External Dependencies

### Core Dependencies
- **Python Standard Library**: 
  - `argparse`: Command-line argument parsing
  - `json`: Data serialization/deserialization
  - `os`: File system operations
  - `typing`: Type hints for better code documentation

### Development Dependencies
- **unittest**: Built-in testing framework
- **tempfile**: For creating temporary test files
- **unittest.mock**: For mocking in tests

### Design Rationale
- **No External Dependencies**: Keeps the application lightweight and reduces installation complexity
- **JSON Storage**: Human-readable, easy to debug, and sufficient for small to medium task lists
- **Standard Library Only**: Ensures maximum compatibility and minimal setup requirements

## Deployment Strategy

### Current Approach
- **Standalone Python Application**: Can be run directly with Python interpreter
- **Local File Storage**: Tasks stored in local JSON files
- **Cross-Platform**: Compatible with Windows, macOS, and Linux

### Installation Methods
1. **Direct Execution**: Run `python todo_cli/main.py [commands]`
2. **Package Installation**: Can be packaged using setuptools for pip installation
3. **Executable Creation**: Can be converted to standalone executable using tools like PyInstaller

### Configuration
- **Default Data File**: `tasks.json` in current directory
- **Configurable Storage**: TaskManager accepts custom file paths
- **Error Handling**: Graceful handling of file I/O errors and JSON parsing issues

### Testing Strategy
- **Unit Tests**: Comprehensive test coverage using unittest
- **Temporary Files**: Tests use temporary files to avoid affecting real data
- **Mocking**: Uses unittest.mock for isolating components during testing

## Future Considerations

The current architecture supports easy extension for:
- Database integration (could replace JSON with SQLite or other databases)
- Multi-user support
- Task categories and tags
- Due dates and reminders
- Export/import functionality
- Web interface integration