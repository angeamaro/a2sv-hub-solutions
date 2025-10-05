# Problem:  Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False  # indica fim de palavra


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def can_build(self, word: str) -> bool:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if not node or not node.end:
                return False
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        words.sort()

        longest = ""
        for word in words:
            if trie.can_build(word):
                if len(word) > len(longest):
                    longest = word
        return longest
