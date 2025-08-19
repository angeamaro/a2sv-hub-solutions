# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2) 
        
        while y != 0:
            summ = x ^ y         
            carry = (x & y) << 1 
            x, y = summ, carry   
        
        return bin(x)[2:]