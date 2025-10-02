# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = {}
        for i, ch in enumerate(s):
            if ch not in pos:
                pos[ch] = []
            pos[ch].append(i)
        
        count = 0
        for word in words:
            prev = -1
            found = True
            for ch in word:
                if ch not in pos:
                    found = False
                    break
                idx_list = pos[ch]
                idx = bisect.bisect_right(idx_list, prev)
                if idx == len(idx_list):  
                    found = False
                    break
                prev = idx_list[idx]
            if found:
                count += 1
        return count
            