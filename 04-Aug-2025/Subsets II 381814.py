# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
       res = []        
        subset = []     

        nums.sort()     # Sort the input to ensure duplicates are adjacent

        def back(i):
            if i >= len(nums):
                # When we reach the end, append a copy of the current subset
                res.append(subset.copy())
                return

            # Include nums[i] in the current subset
            subset.append(nums[i])
            back(i + 1)
            
            subset.pop()  # Backtrack: remove nums[i] to explore the "exclude" path

            # Skip all duplicate values of nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            back(i + 1)

        back(0) 
        return res
            

            