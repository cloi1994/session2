class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if endWord not in wordList:
            return 0
        
        q = [beginWord]
        
        wordList = set(wordList)
        
        step = 0
        
        while q != []:
            step += 1
            
            for _ in range(len(q)):

                word = q.pop(0) 
                listWord = list(word)
                
                for i in range(len(word)):
                    
                    for c in 'abcdefghijklmnopqrstuvwxyz': 
                        listWord[i] = c
                        
                        newWord = ''.join(listWord)
                        
                        if newWord == endWord:
                            return step + 1
                        
                        if newWord not in wordList:
                            continue
                            
                        wordList.remove(newWord)
                        q.append(newWord)
                    listWord = list(word)
            
            
            
        return 0
        
