# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            nex = i + brainpower + 1

            if nex < n:
                solve = points + dp[nex]
            else:
                solve = points

            skip = dp[i + 1]
            dp[i] = max(solve,skip)
        return dp[0]



