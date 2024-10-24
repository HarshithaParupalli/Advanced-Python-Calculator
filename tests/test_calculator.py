import pytest
from plugins.add import Plugin as AddPlugin
from plugins.subtract import Plugin as SubtractPlugin
from plugins.multiply import Plugin as MultiplyPlugin
from plugins.divide import Plugin as DividePlugin
from plugins.sqrt import Plugin as SqrtPlugin
from plugins.power import Plugin as PowerPlugin

# Test Addition
def test_add():
    add_plugin = AddPlugin()
    assert add_plugin.execute(12, 2) == 14.0
    assert add_plugin.execute(4, 5) == 9.0
    assert add_plugin.execute(5, 6) == 11.0

# Test Subtraction
def test_subtract():
    subtract_plugin = SubtractPlugin()
    assert subtract_plugin.execute(12, 2) == 10.0
    assert subtract_plugin.execute(5, 5) == 0.0
    assert subtract_plugin.execute(10, 3) == 7.0

# Test Multiplication
def test_multiply():
    multiply_plugin = MultiplyPlugin()
    assert multiply_plugin.execute(4, 5) == 20.0
    assert multiply_plugin.execute(3, 7) == 21.0
    assert multiply_plugin.execute(0, 100) == 0.0

# Test Division
def test_divide():
    divide_plugin = DividePlugin()
    assert divide_plugin.execute(10, 2) == 5.0
    assert divide_plugin.execute(9, 3) == 3.0
    with pytest.raises(ZeroDivisionError):
        divide_plugin.execute(5, 0)

# Test Square Root
def test_sqrt():
    sqrt_plugin = SqrtPlugin()
    assert sqrt_plugin.execute(16) == 4.0
    assert sqrt_plugin.execute(0) == 0.0
    with pytest.raises(ValueError):
        sqrt_plugin.execute(-1)

# Test Power
def test_power():
    power_plugin = PowerPlugin()
    assert power_plugin.execute(2, 3) == 8.0
    assert power_plugin.execute(5, 0) == 1.0
    assert power_plugin.execute(3, 2) == 9.0
