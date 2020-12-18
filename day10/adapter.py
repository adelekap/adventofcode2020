class Adapter:
    def __init__(self, joltage: int):
        self.joltage = joltage

        self.upstream_connections = []
        self.downstream_connections = None

        self.__terminating_nodes = 0

    @property
    def terminating_nodes(self) -> int:
        if not self.downstream_connections:
            return 1
        return self.__terminating_nodes

    def add_terminating_nodes(self, nodes:int):
        self.__terminating_nodes += nodes

    def __hash__(self):
        return self.joltage

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.joltage}'
