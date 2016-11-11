# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 18:59:31 2016

@author: paddy
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        i = 1
        if n == 1:
            return ["1"]
        for i in xrange(1,n):
            if i%15 == 0 :
                l.append("FizzBuzz")
            elif i%5 == 0:
                l.append("Buzz")
            elif i%3 == 0:
                l.append("Fizz")
            else:
                l.append(str(i))
        return l