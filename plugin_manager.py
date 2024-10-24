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
        print("Available commands:", ", ".join(self.plugins.keys()))

    def execute_command(self, command):
        plugin_name, *args = command.split()
        if plugin_name in self.plugins:
            result = self.plugins[plugin_name].execute(*args)
            full_expression = f"{plugin_name} {' '.join(args)}"
            return result, full_expression
        else:
            raise ValueError(f"No such plugin: {plugin_name}")
