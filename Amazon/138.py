# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if not head:
            return head
        
        cur = head

        hm = {}
        
        while cur:
            newNode = RandomListNode(cur.label)
            hm[cur] = newNode
            cur = cur.next
            
        cur = head
        
        while cur:
            hm[cur].next = hm.get(cur.next,None)
            hm[cur].random = hm.get(cur.random,None)
            cur = cur.next
            
        return hm[head]
            
            
