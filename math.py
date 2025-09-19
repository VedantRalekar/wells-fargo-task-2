import numpy as np
array = np.array([[1,2,3,4,5],
                  [2,3,4,6,7]])
arr = np.array([1,2,3,4,5,6])
new_arr = np.delete(array,1,axis=0)
print(new_arr)
print(np.split(arr,3))
print(arr[::-1])

# create a NumPy array using numpy.arange()
print(np.arange(1, 10))

# create a NumPy array using numpy.linspace()
print(np.linspace(1, 10, 3))

# create a NumPy array using numpy.zeros()
print(np.zeros(5, dtype=int))

# create a NumPy array using numpy.ones()
print(np.ones(5, dtype=int))

# create a NumPy array using numpy.random.rand()
print(np.random.rand(5))

# create a NumPy array using numpy.random.randint()
print(np.random.randint(5, size=10))