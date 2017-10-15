import numpy as np


def test_run():
    # List to 1D array
    #print(np.array([2, 3, 4]))

    # List of tuples to 2D array
    #print(np.array([(2, 3, 4), (5, 6, 7)]))

    # Creating an empty array
    #print(np.empty((5, 4)))  # Array will have junk in its memory locations

    # Creating an array of 1s
    #print(np.ones((5,4), dtype = np.int))

    # Creating an array of 0s
    # print(np.zeros((5,4), dtype = np.int))

    # Accessing elements
    #a = np.random.rand(5, 4)
    #print("Array: \n", a)
    # Accessing element at position (3, 2)
    #element = a[3,2]
    # Elements in definned range
    #print(a[0, 1:3])
    # Slicing
    # Note: Slice n:m:t specifies a range that starts at n, and stops before m, in steps of t
    #print(a[:, 0:3:2])  # Will select columns 0, 2 for every row

    # Generate an array full of random numbers, uniformly sampled from [0.0, 1.0)
    #print(np.random.rand(5, 4))  # Alternative method
    #print(np.random.random((5,4)))  # Pass in a size tuple

    # Sample numbers from a Gaussian (normal) distribution
    #print(np.random.normal(size=(2, 3)))  # "Standard normal" (mean = 0, s.dev = 1)
    #print(np.random.normal(50, 10, size=(2, 3)))  # "Standard normal" (mean = 50, s.dev = 10)

    # Random integers
    #print(np.random.randint(10))  # A single integer in [0, 10)
    #print(np.random.randint(0, 10))  # Same as above, specifying [low, high) explicit
    #print(np.random.randint(0, 10, size=5))  # 5 random integers as a 1D array
    #print(np.random.randint(0, 10, size=(2, 3)))  # 2x3 array of random integers

    # Array Attributes
    #a = np.random.rand(5, 4)  # 5x4 random array
    #print(a.size)  # Total entries in the array (20)
    #print(a.shape)  # Returns tuple of array dimensions (5, 4)
    #print(len(a.shape))  # Returns dimensions of a.shape, a.k.a the dimensions of array (2D array)

    # Array Operations
    #np.random.seed(693)  # Seed the random number generator
    #a = np.random.randint(0, 10, size=(5, 4))  # 5x4 random integers in [0, 10)
    #print("Array: \n", a)
    #print("Minimum of each column: \n", a.min(axis=0))
    #print("Maximum of each row: \n", a.max(axis=1))
    #print("Mean of all elements: ", a.mean())  # Leave out axis arg

    # Searching
    #np.random.seed(693)  # Seed the random number generator
    #a = np.random.randint(0, 10, size=(5, 4))  # 5x4 random integers in [0, 10)
    #print("Array: \n", a)
    #print("Index of maximum of each row: \n", np.unravel_index(a.argmax(), a.shape))

    # Masking index arrays
    #a = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0),
    #              (0, 2, 50, 20, 0, 1, 28, 5, 0)])
    #print(a)
    #mean = a.mean()
    # Masking
    #a[a<mean] = mean  # Change every element less than mean to the mean
    #print(a)

    # Arithmetic Operations on Arrays
    a = np.array([(1, 2, 3, 4, 5), (10, 20, 30, 40, 50)])
    print("Original array a: \n", a)
    b = np.array([(100, 200, 300, 400, 500), (1, 2, 3, 4, 5)])
    print("Original array b: \n", b)
    # Multiple a by 2
    print("Multiply a by 2: \n", a * 2)
    # Divide a by 2
    print("Divide a by 2: \n", a / 2)
    # Divide a and b element-wise. Use np.dot(a, b) for matrix multiplication
    print("Multiply a and b: \n", a * b)
    print()


if __name__ == "__main__":
    test_run()