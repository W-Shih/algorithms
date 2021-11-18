# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/159/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 17-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # <Wayne Shih> 17-Nov-2021
        # 4, 5, 6, 7, 0, 1, 2
        # o  o  o  o  x  x  x  <->  o > 2; x <= 2
        if nums is None or len(nums) == 0:
            return -float('inf')

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[-1]:
                l = mid
            else:
                r = mid

        return min(nums[l], nums[r])
