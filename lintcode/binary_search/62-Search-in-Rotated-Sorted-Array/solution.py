# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/62/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 17-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param nums: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if target >= nums[0]:
                if nums[0] <= nums[mid] < target:
                    l = mid
                else:
                    r = mid
            else:
                if target < nums[mid] < nums[0]:
                    r = mid
                else:
                    l = mid

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
