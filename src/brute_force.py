# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

from knapsack import KnapsackInstance, KnapsackSolver

class BruteforceKnapsackSolver(KnapsackSolver):
    """
    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    >>> bfs = BruteforceKnapsackSolver(kp)
    >>> Xopt = bfs.solve()
    >>> Xopt in [(0, 1, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0), (1, 1, 0, 0, 1, 0)]
    True
    >>> bfs.value(Xopt)
    9700
    >>> bfs.weight(Xopt)
    50
    >>> bfs.weight(Xopt) <= bfs._inst.C
    True

    """
    
    def __init__(self, instance) -> None:
        # TODO: write the constructor by calling the parent class constructor
        super().__init__(instance)

    
    def solve(self) -> tuple[int, ...]:
        # solve by brute force
        def possibilities(n:int) -> list[list[int]]:
            if n == 0:
                return [[]]
            else:
                return [[value] + rest for value in [0,1] for rest in possibilities(n-1)]
        for possibility in possibilities(self._inst.size):
            if self.weight(possibility) <= self._inst.C and self.value(possibility) > self.value(self._X):
                sol = self._X  = possibility
        return tuple(sol)
    