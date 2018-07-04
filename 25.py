# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    
    def reverse(self, start, end):
        newhead=ListNode(0); newhead.next=start
        while newhead.next!=end:
            tmp=start.next
            start.next=tmp.next
            tmp.next=newhead.next
            newhead.next=tmp
        return [end, start]
    
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
           
            res = self.reverse(cur.next, end.next)
            
            cur.next = res[0]
            
            cur = res[1]
        
        return root.next
