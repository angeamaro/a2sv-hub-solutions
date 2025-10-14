# Problem: Extra Characters in a String - https://leetcode.com/problems/extra-characters-in-a-string/description/

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dict_set = set(dictionary)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]

            for j in range(i, n):
                if s[i:j+1] in dict_set:
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]
        