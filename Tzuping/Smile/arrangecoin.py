# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 20:44:16 2016

@author: paddy
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = int(((1+8*n)**0.5-1)/2)
        
        return x


