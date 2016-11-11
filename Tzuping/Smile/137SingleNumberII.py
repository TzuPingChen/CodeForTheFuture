# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 15:15:19 2016

@author: paddy
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(2):
            nums.append("more")
        for i in xrange(0,len(nums),3):
            if nums[i] != nums[i+2]:
                return nums[i]