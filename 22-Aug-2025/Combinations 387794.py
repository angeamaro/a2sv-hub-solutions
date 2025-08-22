# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def back(comb, num):
            if len(comb) == k:
                res.append(comb[:])
                return
            if num > n:
                return
            comb.append(num)
            back(comb, num + 1)
            comb.pop()
            back(comb,num + 1)
        back([],1)
        return res



            
        