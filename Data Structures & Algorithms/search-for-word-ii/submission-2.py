class Solution:

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

        def has_child(self, current_node, letter) -> bool:

            idx = ord(letter.lower()) - ord('a')
            if current_node.children[idx] is None:
                return False

            return True

        def is_end_of_word(self, current_node) -> bool:
            
            if not current_node.isEndOfWord:
                return False

            return True

    def is_valid_idx(self, path: List, new_x: int, new_y: int) -> bool:
        if [new_x, new_y] in path:
            return False

        if new_x >= len(self.board[0]) or new_x < 0:
            return False

        if new_y >= len(self.board) or new_y < 0:
            return False

        return True

    def backtrack(self, start_x: int, start_y: int, path: List, current_node):
        
        if not self.trie.has_child(current_node, self.board[start_y][start_x]):
            return

        idx = ord(self.board[start_y][start_x].lower()) - ord('a')
        current_node = current_node.children[idx]

        if self.trie.is_end_of_word(current_node):
            self.result.add("".join([self.board[y][x] for x, y in path]))

        if self.is_valid_idx(path, start_x + 1, start_y):
            path.append([start_x + 1, start_y])
            self.backtrack(start_x + 1, start_y, path, current_node)
            path.pop()

        if self.is_valid_idx(path, start_x, start_y + 1):
            path.append([start_x, start_y + 1])
            self.backtrack(start_x, start_y + 1, path, current_node)
            path.pop()

        if self.is_valid_idx(path, start_x - 1, start_y):
            path.append([start_x - 1, start_y])
            self.backtrack(start_x - 1, start_y, path, current_node)
            path.pop()

        if self.is_valid_idx(path, start_x, start_y - 1):
            path.append([start_x, start_y - 1])
            self.backtrack(start_x, start_y - 1, path, current_node)
            path.pop()

        return


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        self.result = set()
        self.trie = self.PrefixTree()
        self.board = board

        for word in words:
            self.trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[i])):
                self.backtrack(j, i, [[j, i]], self.trie.head)

        return list(self.result)

        