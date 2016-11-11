# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:05:34 2016

@author: paddy
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n%4
        if num == 0:
            return False
        return True
        
n = Solution()
d= n.canWinNim(7)
print d
