# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/521/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 19-Nov-2021  Wayne Shih              Initial create
# 21-Sep-2022  Wayne Shih              Add another solution by hash
# $HISTORY$
# =================================================================================================


class Solution:

    def deduplication_by_ptrs(self, nums):
        """
        @param nums: an array of integers
        @return: the number of unique integers
        """
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

    def deduplication_by_hash(self, nums):
        """
        @param nums: an array of integers
        @return: the number of unique integers
        """
        # <Wayne Shih> 21-Sep-2022
        # - fast ptr moves faster and takes a look to
        #   find the number not in the isDup yet
        # - slow ptr means there are no duplicates on LHS of slow including slow
        if not nums:
            return 0

        unique_num_set = set()
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] in unique_num_set:
                continue

            unique_num_set.add(nums[fast])
            nums[slow] = nums[fast]
            slow += 1

        return slow
