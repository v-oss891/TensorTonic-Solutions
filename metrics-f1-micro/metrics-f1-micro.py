import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    if len(y_true) != len(y_pred):
        return None
        
    y_true=np.array(y_true)
    y_pred=np.array(y_pred)
    tp=np.sum(y_pred== y_true)
    return tp/(len(y_true))
    
    