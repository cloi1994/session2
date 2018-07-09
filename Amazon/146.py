class Node(object):
    def __init__(self, k, v):
        self.prev = None
        self.next = None
        self.key = k
        self.val = v

class DoublyLinkedList(object):
    def __init__(self):
        self.head = Node(0, 0) # head is a dummy head node
        self.tail = Node(0, 0) # tail is a dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove_tail(self):
        old_tail = self.tail.prev
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return old_tail

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hm = {}
        self.dll = DoublyLinkedList()
        self.capacity = capacity
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hm:
            return -1 
        
        node = self.hm[key]
        
        self.dll.remove_node(node)
        self.dll.add_to_head(node)
        
        return node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        newNode = Node(key,value)
        
        if key in self.hm:
            self.dll.remove_node(self.hm[key])
            
        else:
            # current is full, so remove least freq
            if len(self.hm) == self.capacity:
                oldNode = self.dll.remove_tail()
                self.hm.pop(oldNode.key)
            
        self.dll.add_to_head(newNode)
        self.hm[key] = newNode
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
