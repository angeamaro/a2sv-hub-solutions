# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []

        num_to_char = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        comb = []

    
        def back(i):
            if i == len(digits):
                res.append("".join(comb))
                return

            # Iterate over possible letters for the current digit
            for char in num_to_char[digits[i]]:
                comb.append(char)
                back(i + 1)
                comb.pop() 

        back(0)
        return res
        