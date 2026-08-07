class Solution:

    class PrefixTree:

        class TrieNode:

            def __init__(self):
                self.children = [None] * 26
                self.isEndOfWord = False
                self.total_word = None

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
            current.total_word = word

        def has_child(self, current_node, idx) -> bool:

            if current_node.children[idx] is None:
                return False

            return True

        def is_end_of_word(self, current_node) -> bool:
            
            if not current_node.isEndOfWord:
                return False

            return True

    def is_valid_idx(self, new_x: int, new_y: int) -> bool:
        if new_x >= len(self.board[0]) or new_x < 0:
            return False

        if new_y >= len(self.board) or new_y < 0:
            return False

        if self.marked_board[new_y][new_x]:
            return False

        return True

    def backtrack(self, start_x: int, start_y: int, current_node):
        
        idx = ord(self.board[start_y][start_x].lower()) - ord('a')
        if not self.trie.has_child(current_node, idx):
            return

        current_node = current_node.children[idx]

        if self.trie.is_end_of_word(current_node):
            self.result.add(current_node.total_word)

        if self.is_valid_idx(start_x + 1, start_y):
            self.marked_board[start_y][start_x + 1] = True
            self.backtrack(start_x + 1, start_y, current_node)
            self.marked_board[start_y][start_x + 1] = False

        if self.is_valid_idx(start_x, start_y + 1):
            self.marked_board[start_y + 1][start_x] = True
            self.backtrack(start_x, start_y + 1, current_node)
            self.marked_board[start_y + 1][start_x] = False

        if self.is_valid_idx(start_x - 1, start_y):
            self.marked_board[start_y][start_x - 1] = True
            self.backtrack(start_x - 1, start_y, current_node)
            self.marked_board[start_y][start_x - 1] = False

        if self.is_valid_idx(start_x, start_y - 1):
            self.marked_board[start_y - 1][start_x] = True
            self.backtrack(start_x, start_y - 1, current_node)
            self.marked_board[start_y - 1][start_x] = False

        return


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        self.result = set()
        self.trie = self.PrefixTree()
        self.board = board
        self.marked_board = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for word in words:
            self.trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[i])):
                self.marked_board[i][j] = True
                self.backtrack(j, i, self.trie.head)
                self.marked_board[i][j] = False

        return list(self.result)

        