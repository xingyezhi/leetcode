__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total=index=0
        for i in range(2*len(gas)):
            total+=(gas[i%len(gas)]-cost[i%len(gas)])
            if total<0:
                index=i+1
                total=0
                if index>=len(gas):
                    break
        if index>=len(gas):return -1
        else:return index



t=[1,2,3,4,5]
sol=Solution()