import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    X=np.array(X)
    return np.corrcoef(X,rowvar=False)
    pass