class Plugin:
    def execute(self, *args):
        try:
            return sum(map(float, args))
        except ValueError:
            return "Invalid input"
