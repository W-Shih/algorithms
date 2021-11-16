# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/61/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 15-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return [-1, -1]

        left_index = self._search_first_position_of_target(A, target)
        if left_index == -1:
            return [-1, -1]

        right_index = self._search_last_position_of_target(A, target)
        return [left_index, right_index]

    def _search_first_position_of_target(self, nums, target):
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:  # nums[mid] == target
                r = mid

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1

    def _search_last_position_of_target(self, nums, target):
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:  # nums[mid] == target
                l = mid

        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        return -1
