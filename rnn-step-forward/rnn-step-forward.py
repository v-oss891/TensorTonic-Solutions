import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    x_t=np.array(x_t)
    h_prev=np.array(h_prev)
    pre=x_t@Wx+h_prev@Wh+b
    h=np.tanh(pre)
    return h
    
    pass
