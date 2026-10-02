import numpy as np 

def expected_value_discrete(x, p) :
    x = np.asarray(x, dtype = float)
    p = np.asarray(p, dtype = float)
    return float(np.dot(x, p))