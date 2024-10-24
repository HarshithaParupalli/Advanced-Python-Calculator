import pandas as pd

class HistoryManager:
    def __init__(self):
        # Initialize an empty DataFrame with the correct columns
        self.history = pd.DataFrame(columns=["Expression", "Result"])

    def log_calculation(self, expression, result):
        # Create a DataFrame entry for the new calculation
        new_entry = pd.DataFrame({"Expression": [expression], "Result": [result]})
        
        # Concatenate only if the history is not empty
        if not self.history.empty:
            self.history = pd.concat([self.history, new_entry], ignore_index=True)
        else:
            # If history is empty, set it directly to the new entry
            self.history = new_entry

    def show_history(self):
        if self.history.empty:
            print("No history available.")
        else:
            print(self.history)

    def clear_history(self):
        # Clear the history by resetting the DataFrame
        self.history = pd.DataFrame(columns=["Expression", "Result"])

    def save_history(self, file_path):
        # Save the history to a CSV file
        self.history.to_csv(file_path, index=False)

    def load_history(self, file_path):
        # Load history from a CSV file, if it exists
        try:
            self.history = pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"File {file_path} not found. Starting with empty history.")
            self.history = pd.DataFrame(columns=["Expression", "Result"])
