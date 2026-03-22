import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    a=np.array(y_pred)
    b=np.array(y_true)
    return np.sum((abs(a-b))**2)/len(a)
    
