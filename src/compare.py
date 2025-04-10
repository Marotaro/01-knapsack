from knapsack import KnapsackInstance
from brute_force import BruteforceKnapsackSolver
from greedy import GreedyKnapsackSolver

#setup instance
test_instance_name = "src/test_instances/large_scale/knapPI_1_200_1000_1"
test_instance = KnapsackInstance.from_string(KnapsackInstance.load_instance_data(test_instance_name))


#brute_force method
if False:
    Btf = BruteforceKnapsackSolver(test_instance)
    X_Btf = Btf.solve()
    print(f"Brute force methode: \n \tX: {X_Btf} \n \tW: {Btf.weight(X_Btf)} / {Btf._inst.C} \n \tV: {Btf.value(X_Btf)}")

#greedy method
if True:
    G = GreedyKnapsackSolver(test_instance)
    X_G = G.solve()
    print(f"Greedy methode: \n \tX: {X_G} \n \tW: {G.weight(X_G)} / {G._inst.C} \n \tV: {G.value(X_G)}")
