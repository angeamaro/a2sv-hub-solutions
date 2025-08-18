# Problem: Break a palindrome - https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""  

        chars = list(palindrome)

        for i in range(n // 2):
            if chars[i] != 'a':
                chars[i] = 'a'
                return "".join(chars)

        chars[-1] = 'b'
        return "".join(chars)
        