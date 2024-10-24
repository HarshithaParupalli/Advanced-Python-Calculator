class Plugin:
    def execute(self, *args):
        if len(args) != 2:
            raise ValueError("Power operation requires exactly two arguments.")
        try:
            base = float(args[0])
            exponent = float(args[1])
            result = base ** exponent
        except ValueError:
            raise ValueError("Invalid input. Both arguments must be numbers.")
        return result
