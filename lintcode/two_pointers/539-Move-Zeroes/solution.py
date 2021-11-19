# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/539/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 19-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # <Wayne Shih> 19-Nov-2021
        # two pts in the same direction
        # eye pt moves faster and takes a look
        # i pt means LHS of i are all non-zone numbers already
        if nums is None or len(nums) == 0:
            return

        i = 0
        for eye in range(len(nums)):
            if nums[eye] == 0:
                continue
            nums[i], nums[eye] = nums[eye], nums[i]
            i += 1

        return
