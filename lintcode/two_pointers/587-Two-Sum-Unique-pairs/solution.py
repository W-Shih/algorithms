# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/587/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 20-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if nums is None or len(nums) < 2:
            return 0

        nums.sort()

        count = 0
        l, r = 0, len(nums) - 1
        while l < r:
            two_sum = nums[l] + nums[r]
            if two_sum == target:
                count += 1
                l, r = l + 1, r - 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif two_sum < target:
                l += 1
            else:
                r -= 1

        return count
