# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/585/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 17-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return float('inf')

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2 # 1 <= mid <= len(nums) - 2
            if nums[mid] > nums[mid - 1]:
                l = mid
            else:
                r = mid

        return max(nums[l], nums[r])
