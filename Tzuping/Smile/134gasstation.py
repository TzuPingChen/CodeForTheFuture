# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 17:10:32 2016

@author: paddy
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1
        startpoint = 0
        Tgas = 0
        for i in range(len(gas)):
            if gas[i] + Tgas < cost[i]:
                startpoint = i+1
                Tgas = 0
            else:
                Tgas += gas[i]-cost[i]
        return startpoint


       
        
gas = [1,2,3,3]
cost = [2,1,5,1]
x = Solution()
y = x.canCompleteCircuit(gas,cost)
print y