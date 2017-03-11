import functools
import numpy as np


print(functools.reduce(lambda val, n: val * ((1 + 0.01) if np.random.choice([-1, 1]) > 0 else (1 - 0.01)),
                       [i for i in range(1, 30)], 100))
