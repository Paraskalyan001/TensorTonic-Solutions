import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    n = np.array(x)
    s = 1/(1+(np.exp(-n)))
    return s
    pass