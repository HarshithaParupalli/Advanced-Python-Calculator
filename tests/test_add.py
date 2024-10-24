import pytest
from plugins.add import Plugin

def test_add():
    plugin = Plugin()
    result = plugin.execute(2, 3)
    assert result == 5

def test_invalid_input():
    plugin = Plugin()
    result = plugin.execute("a", 3)
    assert result == "Invalid input"
