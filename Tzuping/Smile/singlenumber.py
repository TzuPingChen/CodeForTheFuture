# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 19:28:00 2016

@author: paddy
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) ==2:
            return False
        
        nums.sort()
        nums.append("i love python")
        for i in xrange(0,len(nums),2):
            if nums[i] != nums[i+1]:
                return nums[i]

        
nums = [1,-1,1,3,-1]
sol = Solution()
print sol.singleNumber(nums)