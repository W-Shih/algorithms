# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/75/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 17-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if A is None or len(A) < 3:
            return -1

        l, r = 0, len(A) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            # find one peak
            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid

            if A[mid] > A[mid - 1]:
                l = mid
            else:
                r = mid

        return l if A[l] > A[r] else r
