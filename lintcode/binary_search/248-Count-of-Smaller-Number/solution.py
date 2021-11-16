# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/248/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 15-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # <Wayne Shih> 15-Nov-2014
        # 在 python 中:
        #   None, '', [], {}, (), 0, False 皆等價於 False
        #   i.e. not None == not '' == not [] == not {} == not () == not 0 == not False == True
        # 所以 'if not nums' 無法分辨 nums == None / nums == []
        # 本題看似無傷大雅, 但若是題目需求上需要區分 nums == None / nums == []
        # 'if not nums' 的寫法則有可能因此埋下 bug
        if A is None or len(A) == 0:
            return [0] * len(queries)

        A.sort()
        results = []
        for target in queries:
            count = self._get_count_of_smaller_number(A, target)
            results.append(count)
        return results

    def _get_count_of_smaller_number(self, sorted_nums, target):
        # <Wayne Shih> 15-Nov-2014
        # find the first number in A >= target
        l, r = 0, len(sorted_nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if sorted_nums[mid] >= target:
                r = mid
            else:
                l = mid

        if sorted_nums[l] >= target:
            return l
        if sorted_nums[r] >= target:
            return r
        return len(sorted_nums)
