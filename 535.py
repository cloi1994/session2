import random

class Codec:
    
    def __init__(self):
        self.code2url = {}
        self.url2code = {}
        
        

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.url2code:
            return self.url2code[longUrl]
        
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        
        while longUrl not in self.url2code:
            
            tmp = ""
            
            for _ in range(6):
                tmp += alpha[random.randint(0,25)]
                
            if tmp not in self.code2url:
                self.url2code[longUrl] = tmp
                self.code2url[tmp] = longUrl
                
        
        return 'tiny.com/' + self.url2code[longUrl]
        
        
    
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
