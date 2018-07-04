# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    
    def reverse(self, start, end,k):
                
        cur = start
        prev = end.next
        
        for _ in range(k):
            curNext = cur.next
            cur.next = prev
            prev = cur
            cur = curNext
        
        return [prev, start]
    
    def reverseKGroup(self, head, k):
        if not head: 
            return None
        
        root = ListNode(0) 
        
        root.next = head
        
        cur = root
        
        while cur.next:
            
            end = cur
            
            for i in range(k-1):
                
                end = end.next
                
                if not end.next:
                    return root.next 
                
            res = self.reverse(cur.next, end.next,k)    
            
            cur.next = res[0]
            
            cur = res[1]
        
        return root.next
