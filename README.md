# Advanced Python Calculator

## Overview
This is an advanced Python calculator with a command-line interface (REPL), dynamic plugin system, calculation history management using Pandas, and comprehensive logging.

## Setup Instructions
1. Clone the repository and navigate into the project directory:
    ```bash
    git clone <your-repo-url>
    cd advanced-python-calculator
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the calculator:
    ```bash
    python calc.py
    ```

## Design Patterns
- **Command Pattern**: Plugins use the command pattern to execute user commands dynamically.
- **Facade Pattern**: The `HistoryManager` simplifies interaction with Pandas for managing history.
- **Singleton Pattern**: The logger is implemented as a singleton to ensure consistent logging.

## Logging
Logging is configured using environment variables and writes logs to a file in the `logs/` directory. Log level and log file destination can be configured via the `.env` file.

## Testing
Run tests with Pytest:
```bash
pytest
