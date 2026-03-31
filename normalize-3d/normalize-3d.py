import numpy as np

def normalize_3d(v):
    x = np.array(v, dtype=float)
    
    norms = np.linalg.norm(x, axis=-1, keepdims=True)
    
    safe_norms = np.where(norms > 1e-10, norms, 1.0)
    
    normalized = x / safe_norms
    
    
    normalized = np.where(norms > 1e-10, normalized, 0.0)
    
    return normalized