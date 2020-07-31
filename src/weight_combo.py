import itertools
import numpy as np

weights = [90,90,70,20,20,50,10,5]
bar_weight = 45

bar_plus_weight = [[sum(i) + bar_weight for i in list(itertools.combinations(weights, j))] for j in range(len(weights)+1)]
flatten = lambda l: [item for sublist in l for item in sublist]
weight_combos = np.array(list(dict.fromkeys(flatten(bar_plus_weight))))
weight_combos.sort()

print(weight_combos)
