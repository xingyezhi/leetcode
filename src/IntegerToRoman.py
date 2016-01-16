__author__ = 'lenovo'
# coding=utf-8
class Solution:
    # @param {integer} num
    # @return {string}
    def getNumber(self,A,B,C,N):
        if N==9:
            return A+C
        elif N==0:
            return ""
        elif N==5:
            return B
        elif N==4:
            return A+B
        elif 6<=N<=8:
            return B+A*(N-5)
        else:
            return A*N

    def intToRoman(self, num):
        aNumber=[0,0,0,0]
        counts=0
        while num!=0:
            aNumber[counts]=num%10
            num/=10
            counts+=1
        result=""
        result+='M'*aNumber[3]
        result+=self.getNumber('C','D','M',aNumber[2])
        result+=self.getNumber('X','L','C',aNumber[1])
        result+=self.getNumber('I','V','X',aNumber[0])
        return result

sol=Solution()
print sol.intToRoman(1000)