# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:17:38 2016

@author: paddy
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtype = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    rtype = [i,j]
                    return rtype

s = Solution()
p = s.twoSum([3,2,4],6)
print p 