import math

class Plugin:
    def execute(self, *args):
        if len(args) != 1:
            raise ValueError("Square root operation requires exactly one argument.")
        try:
            number = float(args[0])
            if number < 0:
                raise ValueError("Cannot calculate square root of a negative number.")
            result = math.sqrt(number)
        except ValueError:
            raise ValueError("Invalid input. Argument must be a number.")
        return result
