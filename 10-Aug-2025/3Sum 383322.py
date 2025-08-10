# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate i

            j, k = i + 1, len(nums) - 1
            while j < k:

                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total < 0:
                    j += 1
                    
                else:
                    k -= 1

        return res
