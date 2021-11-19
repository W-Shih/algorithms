# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/521/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 19-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # <Wayne Shih> 19-Nov-2021
        # - sort first
        # - eye ptr moves faster and takes a look to
        #   find the number different than the num that i ptr points to
        # - i ptr means there are no duplicates on LHS of i including i
        if nums is None or len(nums) == 0:
            return 0

        nums.sort()
        i = 0
        for eye in range(1, len(nums)):
            if nums[eye] == nums[i]:
                continue
            nums[i + 1], nums[eye] = nums[eye], nums[i + 1]
            i = i + 1

        return i + 1
