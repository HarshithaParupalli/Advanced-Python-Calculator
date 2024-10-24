class Plugin:
    def execute(self, *args):
        if len(args) != 2:
            raise ValueError("Multiply operation requires exactly two arguments.")
        try:
            result = float(args[0]) * float(args[1])
        except ValueError:
            raise ValueError("Invalid input. Both arguments must be numbers.")
        return result
