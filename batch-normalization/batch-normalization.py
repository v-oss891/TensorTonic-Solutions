import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x=np.array(x)
    gamma=np.array(gamma)
    beta=np.array(beta)
    if x.ndim==2:
        m=np.mean(x,axis=0,keepdims=True)
        v=np.var(x,axis=0,keepdims=True)
    elif x.ndim==4:
        m=np.mean(x,axis=(0,2,3),keepdims=True)
        v=np.var(x,axis=(0,2,3),keepdims=True)
    else:
        raise ValueError("Unsupported shape")
    x_hat=(x-m)/np.sqrt(v+eps)
    if x.ndim == 4:
        gamma = gamma.reshape(1, -1, 1, 1)
        beta  = beta.reshape(1, -1, 1, 1)
    out=gamma*x_hat+beta
    return out
    
        