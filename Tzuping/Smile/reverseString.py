# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 19:16:48 2016

@author: paddy
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stringlist = list(s);
        i = 0
        ans = []
        len(stringlist)
        while i < (len(stringlist)):
            ans.append(s[len(stringlist)-1-i])
            i+=1
        answer =''.join(ans)
        return answer
            