import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X=np.array(X)
    if X.ndim!=2:
        return None
    N=X.shape[0]
    if N<2:
        return None
    m=np.mean(X,axis=0)
    x_centered=X-m
    x_centered_t=x_centered.T
    
    
    var=(x_centered_t@x_centered)/(N-1)
    return var
  