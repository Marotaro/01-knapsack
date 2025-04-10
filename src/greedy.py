# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

from knapsack import KnapsackInstance, KnapsackSolver

class GreedyKnapsackSolver(KnapsackSolver):
    """
    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    >>> bfs = GreedyKnapsackSolver(kp)
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
        super().__init__(instance)

    
    def solve(self) -> tuple[int, ...]:
        # solve by greedy method
        ratio = list(map(lambda weight, value: value/weight, self._inst.W, self._inst.V))
        sorted_index_ration = sorted(list(enumerate(ratio)), key = lambda x: x[1], reverse=True)
        C_cap = 0
        for i, _ in sorted_index_ration:
            C_cap += self._inst.W[i]
            if C_cap > 50:
                break
            else:
                self._X[i] = 1
        return tuple(self._X)