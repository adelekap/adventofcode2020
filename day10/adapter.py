class Adapter:
    def __init__(self, joltage: int):
        self.joltage = joltage

        self.upstream_connections = []
        self.downstream_connections = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.joltage}'
