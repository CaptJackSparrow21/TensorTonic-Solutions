import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    X = np.asarray(X, dtype=float)
    mean = np.mean(X, axis=axis, keepdims=True)
    std = np.std(X, axis=axis, keepdims=True)
    safe_std = np.where(std > eps, std, 1.0)
    return (X - mean) / safe_std