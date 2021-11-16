# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/457/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 14-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def find_position(self, nums, target):
        # <Wayne Shih> 11-Nov-2014
        # 在 python 中:
        #   None, '', [], {}, (), 0, False 皆等價於 False
        #   i.e. not None == not '' == not [] == not {} == not () == not 0 == not False == True
        # 所以 'if not nums' 無法分辨 nums == None / nums == []
        # 本題看似無傷大雅, 但若是題目需求上需要區分 nums == None / nums == []
        # 'if not nums' 的寫法則有可能因此埋下 bug
        if nums is None or len(nums) == 0:
            return -1

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                l = mid
            else: # nums[mid] > target
                r = mid

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
        