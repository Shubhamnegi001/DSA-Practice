class Solution:
    def matrixReshape(self, mat,r,c):
        import numpy as np
        a = np.array(mat)
        if a.size != r*c:
            return mat
        result = a.reshape(r,c)
        return result.tolist()
        
        