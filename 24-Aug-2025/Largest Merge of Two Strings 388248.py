# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        s = ""
        i = j = 0
        n, m = len(word1), len(word2)

        while i < n and j < m:
            if word1[i] > word2[j]:
                s += word1[i]
                i += 1
            elif word1[i] < word2[j]:
                s += word2[j]
                j += 1
            else:
                if word1[i:] > word2[j:]:  
                    s += word1[i]
                    i += 1
                else:
                    s += word2[j]
                    j += 1
        
        if i < n:
            s += word1[i:]

        if j < m:
            s += word2[j:]
        return s

        