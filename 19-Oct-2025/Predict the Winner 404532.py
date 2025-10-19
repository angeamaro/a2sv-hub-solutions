# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def backtrack(left, right, turn):
            if left == right:
                return nums[left] * turn

            pick_left = nums[left] * turn + backtrack(left + 1, right, -turn)
            pick_right = nums[right] * turn + backtrack(left, right - 1, -turn)

            if turn == 1:
                return max(pick_left, pick_right)
            else:
                return min(pick_left, pick_right)

        
        return backtrack(0, len(nums) - 1, 1) >= 0