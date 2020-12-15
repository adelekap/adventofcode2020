class InfeasibleSolutionException(Exception):
    """
    Exception raised when no feasible solution can be found
    given the puzzle input.
    """

    def __str__(self):
        return 'No feasible solution found!'

    def __repr__(self):
        str(self)
