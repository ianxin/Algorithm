    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
 #倒序遍历list   
def removeElement(self, A, elem):
        # write your code here
        for i in range(len(A)-1,-1,-1):
            if A[i] == elem:
                A.pop(i)
        return len(A)
    
    
   #遍历拷贝的list ，操作原始list
   def removeElement(self, A, elem):
        # write your code here
        for i in A[:]:
            if i == elem:
                A.remove(i)
        return len(A)
