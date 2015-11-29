__author__ = 'xingyezhi'
# encoding: utf-8
class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs)==0:
            return []
        strs.sort()
        strlist=[]
        for i in range(len(strs)):
            temp=list(strs[i])
            temp.sort()
            strlist.append(("".join(temp),i,strs[i]))
        strlist.sort(key=lambda x:(x[0],x[1]))
        result,middle=[],[]
        temp=strlist[0][0]
        middle.append(strlist[0][2])
        for pair in strlist[1:]:
            if pair[0]==temp:
                middle.append(pair[2])
            else:
                result.append(middle)
                middle=[pair[2]]
                temp=pair[0]
        result.append(middle)
        return result

sol=Solution()
print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
