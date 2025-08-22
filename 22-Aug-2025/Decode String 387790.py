# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string = ""
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)  
            elif c == "[":
                stack.append((string, num))
                string = ""
                num = 0
            elif c == "]":
                prev, k = stack.pop()
                string = prev + k * string
            else:  
                string += c

        return string
        