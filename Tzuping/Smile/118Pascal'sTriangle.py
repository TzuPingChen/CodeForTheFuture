# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:36:21 2016

@author: paddy
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
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
        n = numRows
        ans = [[1]]
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        for row in xrange(1,n,1):
            temp = []
            for j in range(row+1):
                element = combination(row,j)
                temp.append(element)
            ans.append(temp)
        return ans
            
            