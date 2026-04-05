import numpy as np
def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    n=len(X[0])
    X=np.array(X)
    y=np.array(y)
    a=(X.T@X)+lam*np.eye(n)
    a=np.linalg.inv(a)
    w=a@X.T@y
    return w