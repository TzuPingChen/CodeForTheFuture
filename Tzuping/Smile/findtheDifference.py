# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 20:19:42 2016

@author: paddy
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ts = sorted(s)
        tt = sorted(t)
        sli = list(ts)
        tli = list(tt)
        for i in range(len(sli)):
            if sli[i] != tli[i]:
                return tli[i]
                
        return tli[-1]