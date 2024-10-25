# Advanced Python Calculator

## Overview
This is an advanced Python calculator with a command-line interface (REPL), a dynamic plugin system, calculation history management using Pandas, and comprehensive logging and testing capabilities. The project is designed with extensibility and maintainability in mind, incorporating several design patterns to handle operations efficiently.

## Setup Instructions
1. **Clone the repository** and navigate into the project directory:
    ```bash
    git clone <repo-url>
    cd advanced-python-calculator
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  ️# For Linux/macOS
    venv\Scripts\activate     # For Windows
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the calculator**:
    ```bash
    python calc.py
    ```

## Usage

Start the REPL environment to interact with the calculator. Available commands include:

- **menu**: Lists available commands and plugins.
- **history**: Displays calculation history.
- **clear history**: Clears the calculation history.
- **delete history**: Deletes specific entries from history.
- **{operation} {args}**: Executes a calculation (e.g., `add 3 5`).

## Design Patterns

- **Command Pattern**: The plugin architecture uses the Command Pattern, enabling each plugin to act as a command that users can execute in the REPL environment dynamically.
  
- **Facade Pattern**: The `HistoryManager` class simplifies interactions with Pandas, abstracting the complexities of data operations, such as loading, saving, and deleting records, to provide an easy-to-use interface.

- **Singleton Pattern**: A singleton logger instance is used to ensure consistent logging across the application. This pattern guarantees that only one instance of the logger exists, allowing centralized control over logging configurations.

## Environment Variables

Environment variables are used for configuration, making the application flexible and adaptable to different environments. You can define variables such as `LOG_LEVEL` and `HISTORY_FILE_PATH` in a `.env` file to customize logging and file storage.

- **Implementation**: Environment variables are accessed in [calc.py](calc.py) and [plugin_manager.py](plugin_manager.py) using Python’s `os` library. 

## Logging

Logging is essential for tracking application operations and errors without halting execution. Logs are written to a file in the `logs/` directory. Configure log levels and destinations in the `.env` file.

- **Example Usage**: See [calc.py](calc.py) for overall logging setup and [plugin_manager.py](plugin_manager.py) for logging specific plugin actions.

## Error Handling

The application leverages two main error-handling strategies:

- **Look Before You Leap (LBYL)**: Checks for command availability in the REPL before attempting execution. For example, verifying that a command exists in `PluginManager` before attempting to execute it.

- **Easier to Ask for Forgiveness than Permission (EAFP)**: Used in individual plugins where input might be unstructured or unexpected, capturing and handling exceptions directly during execution.

- **Example**: [Error handling examples in calc.py](calc.py)

## Calculation History Management with Pandas

History is managed using the Pandas library, allowing users to save, load, clear, and delete history records for easy retrieval and tracking of calculations. History can be managed via REPL commands (`history`, `clear history`, `delete history`).

- **Implementation**: See [HistoryManager](history_manager.py) for methods that handle history operations.

## Testing

Unit tests are written with Pytest, covering both individual plugins and the overall functionality of the REPL. To run tests, use:

```bash
pytest
