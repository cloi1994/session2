# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        
        counter = 0
        
        cur = root
        
        count = [0] * k
        
        res = [None] * k
        
        while cur:
            count[counter%k] += 1
            cur = cur.next
            counter += 1
            
        cur = root
        index = 0
        
        for c in count:
            
            if cur == None:
                return res
            
            res[index] = cur
            
            for i in range(c-1):
                cur = cur.next
            
            nextStart = cur.next
            cur.next = None
                
            cur = nextStart
            index += 1
            
            
            
        return res
            
