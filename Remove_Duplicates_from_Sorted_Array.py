class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 1
        else:
            p = 0
            n = len(A)
            for i in range(1,n):
                if A[p] != A[i]:
                    p += 1
                    A[p] = A[i]
                    
            return p + 1








