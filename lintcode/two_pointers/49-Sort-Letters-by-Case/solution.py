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
            while l <= r and self._is_char_lower(chars[l]):
                l += 1
            while l <= r and self._is_char_upper(chars[r]):
                r -= 1

            if l <= r:
                chars[l], chars[r] = chars[r], chars[l]
                l, r = l + 1, r - 1

    def _is_char_lower(self, char):
        if 'a' <= char <= 'z':
            return True
        return False

    def _is_char_upper(self, char):
        if 'A' <= char <= 'Z':
            return True
        return False
