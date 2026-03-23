import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y=np.array(y)
    _, counts = np.unique(y, return_counts=True)
    p=counts/counts.sum()
    if -np.sum(p * np.log2(p + 1e-12))<0:
        return 0.0 
        
    return -np.sum(p * np.log2(p + 1e-12))