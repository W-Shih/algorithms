# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/604/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 21-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        result = []
        if nums is None or len(nums) == 0:
            return result

        if k <= 0 or len(nums) < k:
            return result

        win_sum = 0
        for i in range(k):
            win_sum += nums[i]
        result.append(win_sum)

        for i in range(k, len(nums)):
            win_sum += nums[i] - nums[i - k]
            result.append(win_sum)

        return result
