# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.is_end = False

    class Trie:
        def __init__(self, outer):
            self.root = outer.TrieNode()
    
    def insert(self, root, word):
        node = root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = self.TrieNode()
            node = node.children[index]
        node.is_end = True 

    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # construir o trie
        trie = self.Trie(self)
        for word in strs:
            self.insert(trie.root, word)

        # percorrer até parar
        pref = ""
        node = trie.root
        while node:
            child = []
            for i in range(26):
                if node.children[i]:
                    child.append(i)

            if len(child) != 1 or node.is_end:
                break

            node = node.children[child[0]]
            pref += chr(child[0] + ord('a'))
        
        return pref
