__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def combinationSum(self, candidates, target):
        candidates=sorted(candidates)
        self.candidates=candidates
        return self.getResult(0,target)
    def getResult(self,index,target):
        result=[]
        if target<=0:
            return result
        for i in range(index,len(self.candidates)):
            temp=[]
            if self.candidates[i]>target:
                continue
            elif self.candidates[i]==target:
                temp.append([target])
            else:
                subResult=self.getResult(i,target-self.candidates[i])
                for v in subResult:
                    temp.append([self.candidates[i]]+v)
            for v in temp:
                result.append(v)
        return result

sol=Solution()
print sol.combinationSum([8,7,4,3], 11)
