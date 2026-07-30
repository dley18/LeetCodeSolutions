class PrefixTree:

    class TrieNode:

        def __init__(self):
            self.children = [None] * 26
            self.isEndOfWord = False

    def __init__(self):
        self.head = self.TrieNode()
        
    def insert(self, word: str) -> None:

        current = self.head

        for letter in word:
            idx = ord(letter.lower()) - ord('a')
            if current.children[idx] is None:
                new_node = self.TrieNode()
                current.children[idx] = new_node

            current = current.children[idx]
        
        current.isEndOfWord = True


    def search(self, word: str) -> bool:

        current = self.head

        for letter in word:
            idx = ord(letter.lower()) - ord('a')

            if current.children[idx] is None:
                return False

            current = current.children[idx]
        
        return current.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:

        current = self.head

        for letter in prefix:
             
            idx = ord(letter.lower()) - ord('a')

            if current.children[idx] is None:
                return False

            current = current.children[idx]

        return True
        
        