# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)

        l = 0
        while l < n:
            pos = nums[l] - 1
            if nums[l] != nums[pos]:
                nums[l],nums[pos] = nums[pos],nums[l]
            else:
                l += 1

        res = []

        for i in range(n):
            if nums[i] != i + 1:
                res.append(nums[i])
        return res


        