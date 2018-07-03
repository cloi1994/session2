# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head:
            return True
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        #slow = slow.next
        
        print slow.val
            
        right = self.reverse(slow)
        
        
        left = head
        
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next  
            
        return True
        
        
    def reverse(self,head):
        
        prev = None
        
        cur = head
        
        while cur:
            
            curNext = cur.next
            cur.next = prev
            prev = cur
            cur = curNext
            
        return prev
        
        
        
