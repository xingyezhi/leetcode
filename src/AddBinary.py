__author__ = 'lenovo'
# coding=utf-8
class Solution(object):
    def addBinary(self, a, b):
        a,b=a[::-1],b[::-1]
        temp,result=0,[]
        lens=min(len(a),len(b))
        for i in range(lens):
            result.append((int(a[i])+int(b[i])+temp)%2)
            temp=(int(a[i])+int(b[i])+temp)/2
        for i in a[lens:] if len(a)>len(b) else b[lens:]:
            result.append((temp+int(i))%2)
            temp=(temp+int(i))/2
        if temp!=0:result.append(temp)
        return ''.join([str(i) for i in result[::-1]])


sol=Solution()
print sol.addBinary("11","1")