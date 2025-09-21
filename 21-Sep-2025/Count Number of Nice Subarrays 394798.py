# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1  
        prefix = 0
        res = 0

        for num in nums:
            prefix += num % 2 
            if prefix - k in count:
                res += count[prefix - k]
            count[prefix] += 1
        
        return res