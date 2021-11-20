# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/608/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 19-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return []

        l, r = 0, len(nums) - 1
        while l < r:
            two_sum = nums[l] + nums[r]
            if two_sum == target:
                return [l + 1, r + 1]

            if two_sum < target:
                l += 1
            else:
                r -= 1

        return []
