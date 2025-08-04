# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []        # This will hold all the subsets
        subset = []     # This holds the current subset we're building

        def back(i):
            # Base case: if we've considered all elements
            if i >= len(nums):
                res.append(subset.copy())  # Add a copy of the current subset to the result
                return

            # Include nums[i] in the subset
            subset.append(nums[i])
            back(i + 1)         # Move to the next index

            # Backtrack: remove nums[i] and try without it
            subset.pop()
            back(i + 1)         # Move to the next index without including nums[i]

        back(0)  # Start recursion from index 0
        return res