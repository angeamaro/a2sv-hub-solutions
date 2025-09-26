# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True     
    
    def search(self, word: str) -> bool:
        
        def dfs(idx, node):
            if idx == len(word):
                return node.is_end

            ch = word[idx]
            if ch == ".":
                for child in node.children.values():
                    if dfs(idx + 1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(idx + 1, node.children[ch])

        return dfs(0, self.root)