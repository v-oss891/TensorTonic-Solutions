import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    a=np.array(x1)
    b=np.array(x2)
    c=np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
    if label==1:
        return 1-c
    if label==-1:
        return max(0,c-margin)