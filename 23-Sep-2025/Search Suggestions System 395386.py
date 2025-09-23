# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.sugge = []
        
    def build(self, prod):
        root = self.TrieNode()
        for pr in prod:
            node = root
            for ch in pr:
                index = ord(ch) - ord('a')
                if not node.children[index]:
                    node.children[index] = self.TrieNode()
                node = node.children[index]
                if len(node.sugge) < 3:
                    node.sugge.append(pr)
        return root

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = self.build(products)
        res = []
        node = root

        for ch in searchWord:
            index = ord(ch) - ord('a')
            if node and node.children[index]:
                node = node.children[index]
                res.append(node.sugge)
            else:
                node = None
                res.append([])
        return res



        