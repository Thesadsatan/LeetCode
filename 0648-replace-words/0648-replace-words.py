class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        
        curr = self.root
        
        for char in word:
            if not char in curr.children:
                node = TrieNode()
                curr.children[char] = node
            
            curr = curr.children[char]
        
        curr.end = True
        return self.root
        
        
    def search(self, word):
        
        root = self.root
        replace = ''
        
        for char in word:
            if not char in curr.children and not curr.end:
                return replace
            
            if curr.end:
                return replace
            
            replace += char
            curr = curr.children[char]
        
    

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        words = sentence.split(" ")
        root = Trie()
        
        for word in dictionary:           
            root.insert(word)

        
        for i, word in enumerate(words):
            words[i] = self.search(root.root, word)
        
        return (" ").join(words)
                     
            
    def search(self, root, word):

        curr = root
        replace = ''

        for char in word:
            if not char in curr.children and not curr.end:
                return  word

            if curr.end:
                return replace

            replace += char
            curr = curr.children[char]
        
        return word
            
        
            
            
            
            
            
            
            
                
        