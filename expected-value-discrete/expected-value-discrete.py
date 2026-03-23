import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x=np.array(x)
    p=np.array(p)
    if x.shape!=p.shape:
        return "ValueError"
    if not np.isclose(np.sum(p), 1.0, atol=1e-6):
        raise ValueError("Invalid probabilities")
    return np.sum(x*p)
    
