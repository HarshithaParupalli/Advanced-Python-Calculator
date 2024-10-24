import pandas as pd
import os

class HistoryManager:
    def __init__(self, history_file='history.csv'):
        self.history_file = history_file
        self.history = self.load_history()

    def load_history(self):
        """Load history from a CSV file into a DataFrame."""
        if os.path.exists(self.history_file):
            return pd.read_csv(self.history_file)
        return pd.DataFrame(columns=['Expression', 'Result'])

    def save_history(self):
        """Save the current history DataFrame to a CSV file."""
        self.history.to_csv(self.history_file, index=False)

    def add_entry(self, expression, result):
        """Add a new entry to the history."""
        new_entry = pd.DataFrame({'Expression': [expression], 'Result': [result]})
        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.save_history()

    def clear_history(self):
        """Clear all history records."""
        self.history = pd.DataFrame(columns=['Expression', 'Result'])
        self.save_history()

    def delete_entry(self, index):
        """Delete an entry from the history by index."""
        if 0 <= index < len(self.history):
            self.history = self.history.drop(index).reset_index(drop=True)
            self.save_history()
        else:
            print("Index out of range.")


    def view_history(self):
        """Display the calculation history."""
        return self.history
