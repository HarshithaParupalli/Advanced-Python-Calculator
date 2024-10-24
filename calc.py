from history_manager import HistoryManager
from plugin_manager import PluginManager

def repl():
    history_manager = HistoryManager()
    plugin_manager = PluginManager()

    while True:
        try:
            command = input("calc> ").strip()
            if command == "exit":
                break
            elif command == "history":
                history_manager.show_history()
            elif command == "menu":
                plugin_manager.show_plugins()
            else:
                result, full_expression = plugin_manager.execute_command(command)
                print(f"Result: {result}")
                history_manager.log_calculation(full_expression, result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
