__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    # def grayCode(self, n):
    #     if n==1:return [0,1]
    #     sublist=self.grayCode(n-1)
    #     list=[i*2 for i in sublist]
    #     list.extend([i*2+1 for i in sublist[::-1]])
    #     return list
    def grayCode(self, n):
        result,map=[0],{0:1}
        temp,counts,total=0,1,(1<<n)
        while counts<total:
            for i in range(n):
                mid=temp^(1<<i)
                if not map.has_key(mid):
                    result.append(mid)
                    map[mid]=1
                    temp=mid
                    counts+=1
                    break
        return result



sol=Solution()
#print sol.grayCode(3)
print 3>>1
