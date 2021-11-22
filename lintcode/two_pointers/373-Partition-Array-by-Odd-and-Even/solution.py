# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/373/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 21-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return

        l, r = 0, len(nums) - 1
        while l <= r:
            while l <= r and nums[l] % 2 == 1:
                l += 1
            while l <= r and nums[r] % 2 == 0:
                r -= 1

            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
