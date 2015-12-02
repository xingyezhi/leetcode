__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates=sorted(candidates)
        return self.getResult(candidates,target)

    def getResult(self,candidates,target):
        result=[]
        if target<=0:
            return result
        for i in range(len(candidates)):
            temp=[]
            if i>0 and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                continue
            elif candidates[i]==target:
                temp.append([target])
            else:
                subResult=self.getResult(candidates[i+1:],target-candidates[i])
                for v in subResult:
                    temp.append([candidates[i]]+v)
            for v in temp:
                result.append(v)
        return result
sol=Solution()
print sol.combinationSum2([10,1,2,7,6,1,5],8)