# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        aLen = self.getLength(headA)
        bLen = self.getLength(headB)
        
        diff = abs(aLen - bLen)
        
        if aLen > bLen:
            
            for i in range(diff):
                headA = headA.next
                
        elif bLen > aLen:
            
            for i in range(diff):
                headB = headB.next
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        
        return None
            
        
        
    def getLength(self,head):
        
        count = 0
        
        while head:
            head = head.next
            count += 1
        return count
        
