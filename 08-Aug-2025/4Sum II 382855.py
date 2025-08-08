# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_dict = defaultdict(int)

        for a in nums1:
            for b in nums2:
                sum_dict[a + b] += 1

        res = 0

        for c in nums3:
            for d in nums4:
                num = -(c + d)
                if num in sum_dict:
                    res += sum_dict[num]

        return res

            