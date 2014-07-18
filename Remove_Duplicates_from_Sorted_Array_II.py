class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        n = len(A)
        
        if n == 1:
            return 1
            
        p = 0       # 游标
        IS_TWO = 0  # 某个元素是否第二次出现：0-尚未第二次出现 1-已出现2次
        
        for i in range(1,n):
            
            if A[i] == A[p] and IS_TWO == 0:
                IS_TWO = 1
                p += 1
                A[p] = A[i]
                
            if A[i] != A[p]:
                p += 1
                A[p] = A[i]
                IS_TWO = 0
        
        return p + 1










