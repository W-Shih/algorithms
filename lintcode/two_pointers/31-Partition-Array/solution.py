# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/31/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 21-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        l, r = 0, len(nums) - 1
        while l <= r:
            while l <= r and nums[l] < k:
                l += 1
            while l <= r and nums[r] >= k:
                r -= 1

            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        return l
