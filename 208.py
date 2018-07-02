class Trie(object):
    
    class TrieNode(object):
        def __init__(self):
            self.isWord = False
            self.children = [None] * 26
    

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = Trie.TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        
        p = self.root
        
        
        for c in word:
            index = ord('a') - ord(c)
            
            if not p.children[index]:
                p.children[index] = Trie.TrieNode()
            
            p = p.children[index]
            
        p.isWord = True
        

    def find(self, prefix):
        
        p = self.root
        
        for c in prefix:
            index = ord('a') - ord(c) 
            p = p.children[index]
            if p == None:
                return None
        return p
        
        
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        node = self.find(word)
        
        if node == None or not node.isWord:
            return False
        
        return True
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        node = self.find(prefix)
        
        if node == None:
            return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
