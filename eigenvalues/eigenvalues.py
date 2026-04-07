import numpy as np

def calculate_eigenvalues(matrix):
    try:
        if not isinstance(matrix, (list, tuple)):
            return None
        
        row_lengths = [len(row) for row in matrix if isinstance(row, (list, tuple))]
        if len(row_lengths) == 0 or len(set(row_lengths)) != 1:
            return None
        
        matrix = np.array(matrix)
        
        if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
            return None
        
        if matrix.size == 0:
            return None
        
        eigenvalues = np.linalg.eigvals(matrix)
        idx = np.lexsort((eigenvalues.imag, eigenvalues.real))
        
        return eigenvalues[idx]
    
    except:
        return None