class WordDictionary:

    class Node:
        def __init__(self):
            self.children = [None] * 26
            self.isEndOfWord = False

    def __init__(self):
        self.head = self.Node()

    def addWord(self, word: str) -> None:
        current = self.head

        for letter in word:
            idx = ord(letter.lower()) - ord('a')
            if current.children[idx] is None:
                new_node = self.Node()
                current.children[idx] = new_node
            
            current = current.children[idx]
        
        current.isEndOfWord = True

    def recursive_search(self, word: str, idx: int, current: Node):
        if idx >= len(word):
            return current.isEndOfWord

        if word[idx] == '.':
            for i in range(26):
                if current.children[i] is not None:
                    if self.recursive_search(word, idx + 1, current.children[i]):
                        return True
            return False

        letter_idx = ord(word[idx].lower()) - ord('a')
        if current.children[letter_idx] is None:
            return False

        return self.recursive_search(word, idx + 1, current.children[letter_idx])

    def search(self, word: str) -> bool:
        return self.recursive_search(word, 0, self.head)