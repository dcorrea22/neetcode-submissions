class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()                          
    
    def insert(self, word: str) -> None:
        positions = [ord(char) - 96 for char in word.lower() if char.isalpha()]

        if len(positions) > 0:
            root = self.root

            for number in positions:                
                if root.children[number-1] == None:
                    root.children[number-1] = TrieNode()
                    root = root.children[number-1]
                else:
                    root = root.children[number-1]

            root.endOfWord = True
        
    def search(self, word: str) -> bool:
        root = self.root
        positions = [ord(char) - 96 for char in word.lower() if char.isalpha()]

        for i in positions:
            if root.children[i-1] == None:
                return False
            else:
                root = root.children[i-1]

        return root.endOfWord
    
    def startsWith(self, prefix: str) -> bool:
        root = self.root
        positions = [ord(char) - 96 for char in prefix.lower() if char.isalpha()]

        for i in positions:
            if root.children[i-1] == None:
                return False
            else:
                root = root.children[i-1]

        return True


 
        