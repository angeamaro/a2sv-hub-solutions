# Problem: Reducing Dishes - https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        
        coef = pref = 0
        for data in satisfaction:
            pref += data
            if pref > 0:
                coef += pref
            else:
                break
                
        return coef
        