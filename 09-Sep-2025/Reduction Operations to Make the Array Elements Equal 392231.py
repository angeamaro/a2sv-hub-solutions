# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        aux =list(set(nums))
        aux.sort()
        cont = Counter(nums)
        count = 0
        for i in range(1, len(aux)):
            count += (i * cont[aux[i]])
        return count 

        
       
