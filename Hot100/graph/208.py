from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current_char = self.root
        for char in word:
            if char not in current_char.children:
                current_char.children[char] = TrieNode()
            current_char = current_char.children[char]
        current_char.is_end = True
        

    def search(self, word: str) -> bool:
        current_char = self.root
        for char in word:
            if char not in current_char.children:
                return False
            current_char = current_char.children[char]
        return current_char.is_end
        

    def startsWith(self, prefix: str) -> bool:
        current_char = self.root
        for char in prefix:
            if char not in current_char.children:
                return False
            current_char = current_char.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)