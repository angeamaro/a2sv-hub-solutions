# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        memo = {}

        def back(count, paste):
            if count == n :
                return 0
            if count > n:
                return 1000
            if (count,paste) in memo:
                return memo[(count,paste)]

            count1 = 1 + back(count + paste, paste)
            paste1 =  2 + back( 2 * count, count)
            memo[(count,paste)] = min(count1, paste1)
            return memo[(count,paste)]
        return 1 + back(1,1)
        