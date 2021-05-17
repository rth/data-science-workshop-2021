import numpy as np

rand_array = np.random.rand(10, 3)
rand_array2 = rand_array - 0.75
closest = np.argmin(np.abs(rand_array2), 1)
print(rand_array)
print(closest)