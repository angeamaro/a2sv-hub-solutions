# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # Helper function to validate the additive sequence from index i
        def back(num1: int, num2: int, i: int) -> bool:
            while i < len(num):
                num3 = num1 + num2
                num3_str = str(num3)
                if not num.startswith(num3_str, i):
                    return False
                i += len(num3_str)
                num1, num2 = num2, num3
            return True

        n = len(num)
        # Try all possible splits for the first and second numbers
        for i in range(1, n):
            for j in range(i + 1, n):
                num1, num2 = num[:i], num[i:j]

                # Skip numbers with leading zeros
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue

                if back(int(num1), int(num2), j):
                    return True

        return False