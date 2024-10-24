from history_manager import HistoryManager
from plugin_manager import PluginManager

def repl():
    history_manager = HistoryManager()
    plugin_manager = PluginManager()
    print("Type 'menu' for available commands, 'history' to view the history, 'clear' to clear history, or 'exit' to exit.")
    while True:
        try:
            command = input("calc> ").strip()
            
            if command == "exit":
                break
            elif command == "history":
                print(history_manager.view_history())
            elif command == "clear":
                history_manager.clear_history()
                print("History cleared.")
            elif command.startswith("delete"):
                _, index = command.split()
                history_manager.delete_entry(int(index))
                print(f"Entry {index} deleted.")
            elif command == "menu":
                plugin_manager.show_plugins()
            else:
                result, full_expression = plugin_manager.execute_command(command)
                print(f"Result: {result}")
                history_manager.add_entry(full_expression, result)  

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
