# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/533/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 20-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        # write your code here
        min_diff = float('inf')
        if nums is None or len(nums) == 0:
            return min_diff

        nums.sort()

        l, r = 0, len(nums) - 1
        while l < r:
            two_sum = nums[l] + nums[r]
            if two_sum == target:
                return 0

            min_diff = min(min_diff, abs(target - two_sum))
            if two_sum < target:
                l += 1
            else:
                r -= 1

        return min_diff
