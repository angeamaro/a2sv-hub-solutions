# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution(object):
    def percentageLetter(self, s, letter):
       return s.count(letter) * 100 / len(s)
        