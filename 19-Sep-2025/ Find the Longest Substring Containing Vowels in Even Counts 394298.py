# Problem:  Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        v_dict = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        
        mask = maxi = 0
        seen = {0: -1}   
        
        for i, ch in enumerate(s):
            if ch in v_dict:
                mask ^= (1 << v_dict[ch])   
            
            if mask in seen:
                maxi = max(maxi, i - seen[mask])
            else:
                seen[mask] = i
        
        return maxi
        