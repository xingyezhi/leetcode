__author__ = 'xingyezhi'
# encoding: utf-8


class Solution(object):
    def addResult(self,lencounts,temp,maxWidth):
         if len(temp)!=1:
            spacesize,extra=(maxWidth-lencounts-len(temp)+1)/(len(temp)-1),(maxWidth-lencounts-len(temp)+1)%(len(temp)-1)
            temp_str=temp[0]
            for i in range(1,len(temp)):
                if i<=extra:
                    temp_str+=' '*(spacesize+2)
                    temp_str+=temp[i]
                else:
                    temp_str+=' '*(spacesize+1)
                    temp_str+=temp[i]
         else:
             temp_str=temp[0]
             temp_str+=' '*(maxWidth-len(temp[0]))
         return temp_str
    def fullJustify(self, words, maxWidth):
        result=[]
        lencounts,temp=0,[]
        for i in words:
            lencounts+=len(i)
            if lencounts+len(temp)>maxWidth:
                lencounts-=len(i)
                result.append(self.addResult(lencounts,temp,maxWidth))
                lencounts,temp=len(i),[i]
            else:
                temp.append(i)
        if len(temp)!=0:
            temp_str=temp[0]
            for i in temp[1:]:
                temp_str+=' '+i
            temp_str+=' '*(maxWidth-len(temp_str))
            result.append(temp_str)
        return result


sol=Solution()
print sol.fullJustify(["This"],16)