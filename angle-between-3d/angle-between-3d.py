import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v=np.array(v)
    w=np.array(w)
    if np.linalg.norm(v)*np.linalg.norm(w)==0:
        return np.nan
    s=np.dot(v,w)/(np.linalg.norm(v)*np.linalg.norm(w))
    s=np.clip(s,-1.0,1.0)
    s=np.arccos(s)
    return s
    