# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n =  len(nums)
        prefix =  [0] * n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i - 1] + nums[i]

        if prefix[n - 1] - prefix[0] == 0:
            return 0

        for i in range(1, n):
            if prefix[i - 1] == prefix[n - 1] - prefix[i]:
                return i
        return -1


        