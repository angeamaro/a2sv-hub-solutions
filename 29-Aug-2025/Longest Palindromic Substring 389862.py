# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, longest = 0, 1

        for i in range(n):
            dp[i][i] = True

        for j in range(1, n):        
            for i in range(j):     
                if s[i] == s[j]:
                    if j - i < 3 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if j - i + 1 > longest:
                            start = i
                            longest = j - i + 1

        return s[start:start + longest]