# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/49/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 21-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


from typing import (
    List,
)


class Solution:
    """
    @param chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars: List[str]):
        # write your code here
        if chars is None or len(chars) == 0:
            return

        l, r = 0, len(chars) - 1
        while l <= r:
            while l <= r and chars[l].islower():
                l += 1
            while l <= r and chars[r].isupper():
                r -= 1

            if l <= r:
                chars[l], chars[r] = chars[r], chars[l]
                l, r = l + 1, r - 1
