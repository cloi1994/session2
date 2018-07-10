class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.minStack = []
        self.Stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.Stack.append(x)
        
        if self.minStack == [] or x <= self.minStack[-1]:
            self.minStack.append(x)
            
        

    def pop(self):
        """
        :rtype: void
        """
        
        if not self.Stack:
            return None
        
        if self.minStack != [] and self.Stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        
        return self.Stack.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        
        if not self.Stack:
            return None
        
        return self.Stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.minStack:
            return None
        
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
