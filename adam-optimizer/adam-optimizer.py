import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    param=np.array(param)
    m=np.array(m)
    v=np.array(v)
    grad=np.array(grad)
    a=beta1*m+(1-beta1)*grad
    b=beta2*v+(1-beta2)*(grad**2)
    c=a/(1-beta1**t)
    d=b/(1-beta2**t)
    k=param-lr*c/(np.sqrt(d)+eps)
    return k,a,b
    
