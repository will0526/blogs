from typing import List


class Solution:

    def removeElement(self, nums:List[int], value)->int:

        if not nums:
            return 0

        n = len(nums)
        fast=slow = 0

        while fast < n:
            if nums[fast] != value :
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow
