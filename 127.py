class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        step = 0
        
        wordList = set(wordList)
        
        q = [beginWord]
        
        while q != []:
            
            step += 1
            
            size = len(q)
            
            for _ in range(size):
                
                word = q.pop(0)
                                
                wordInList = list(word)
                
                for i in range(len(word)):
                
                    for letter in 'abcdefghijklmnopqrstuvwxyz':
                        wordInList[i] = letter
                       
                        newWord = ''.join(wordInList)

                        if newWord == endWord:
                            return step + 1

                        if newWord not in wordList:
                            continue
                            
                        wordList.remove(newWord)
                        q.append(newWord)
                        
                        
                    wordInList = list(word)
        return -1
                    
