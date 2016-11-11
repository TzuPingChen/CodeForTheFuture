# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:44:41 2016

@author: paddy
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def factorial(n):
            x = 1
            if n<2:
                return 1
            for i in xrange(1,n+1,1):
                x *= i
            return x
        
        def combination(up,down):
            return factorial(up)/(factorial(down)*factorial(up-down))
        k = rowIndex
        if k ==0:
            return [1]
        ans = []
        for i in range(k+1):
            ele = combination(k,i) 
            ans.append(ele)
        return ans