# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maximum = 0
        n = len(words)
        set_word = [set(word) for word in words]

        for i in range(n):
            for j in range( i + 1 ,n ):
                if set_word[i].isdisjoint(set_word[j]):
                    maximum = max(maximum, len(words[i] * len(words[j])))
                
        return maximum
                    
                
        