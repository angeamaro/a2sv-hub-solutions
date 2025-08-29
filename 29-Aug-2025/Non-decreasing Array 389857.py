# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0  

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if count == 1:
                    return False
                count += 1

                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1] 
                else:
                    nums[i + 1] = nums[i]  

        return True
            