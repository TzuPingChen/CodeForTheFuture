# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 18:12:21 2016

@author: paddy
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k -= len(nums)
        n = -k
        firstpart = nums[n:]
        secondpart = nums[:n]
        for i in range(len(nums)):
            nums.pop()
        nums.extend(firstpart)
        nums.extend(secondpart)
 
            

x = Solution()
s = [1,2]
print s
y = x.rotate(s,3)

print s