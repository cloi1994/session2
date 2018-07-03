import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hm = {}
        self.list = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hm:
            return False
        
        self.list.append(val)
        self.hm[val] = len(self.list) - 1
        
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val not in self.hm:
            return False
        
        targetIndex = self.hm[val]
        
        lastValue = self.list[-1]
                
        
        self.hm[lastValue] = targetIndex
        self.list[targetIndex] = lastValue
        
        
        self.hm.pop(val)
        self.list.pop()        
        return True
        
        
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        
        return self.list[random.randint(0,len(self.list)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
