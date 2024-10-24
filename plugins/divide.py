class Plugin:
    def execute(self, *args):
        if len(args) != 2:
            raise ValueError("Divide operation requires exactly two arguments.")
        try:
            numerator = float(args[0])
            denominator = float(args[1])
            if denominator == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = numerator / denominator
        except ValueError:
            raise ValueError("Invalid input. Both arguments must be numbers.")
        return result
