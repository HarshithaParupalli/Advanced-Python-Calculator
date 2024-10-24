import importlib
import os

class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        for filename in os.listdir("plugins"):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                module = importlib.import_module(f"plugins.{module_name}")
                self.plugins[module_name] = module.Plugin()

    def show_plugins(self):
        available_commands = list(self.plugins.keys()) + ["clear", "delete <index>"]
        print("Available commands:", ", ".join(available_commands))

    def execute_command(self, command):
        # Check if the command is for history management
        if command.startswith("clear"):
            return self.execute_clear()
        elif command.startswith("delete"):
            return self.execute_delete(command)
        
        # Otherwise, treat it as a plugin command
        plugin_name, *args = command.split()
        if plugin_name in self.plugins:
            result = self.plugins[plugin_name].execute(*args)
            full_expression = f"{plugin_name} {' '.join(args)}"
            return result, full_expression
        else:
            raise ValueError(f"No such plugin: {plugin_name}")

    def execute_clear(self):
        return "clear", "History cleared."  # Placeholder response; actual clearing is handled in REPL

    def execute_delete(self, command):
        _, index = command.split()
        return "delete", f"Entry {index} deleted."  # Placeholder response; actual deletion is handled in REPL

