# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:31:02 2016

@author: paddy
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        Ans = [0]*(target+1)
        Ans[0] = 1
        
        for i in range(target+1):
            for num in nums:
                if i+num <= target :
                    Ans[i+num] += Ans[i]
        return Ans[-1]