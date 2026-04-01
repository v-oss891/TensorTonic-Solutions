import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    # Your code here
    points=np.array(points)
    single_point = False
    if points.ndim == 1:
        points = points.reshape(1, 3)
        single_point = True
    
    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]
    
    cos_t = np.cos(theta)
    sin_t = np.sin(theta)
    
    x_new = x * cos_t - y * sin_t
    y_new = x * sin_t + y * cos_t
    z_new = z
    
    rotated = np.stack([x_new, y_new, z_new], axis=1)
    
    if single_point:
        return rotated[0]
    
    return rotated
    
    pass