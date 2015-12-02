__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        str=str.strip();
        if len(str)==0:
            return 0
        begin=sign=result=0
        if str[0]=='+':
            begin=1
        elif str[0].isdigit():
            begin=0
        elif str[0]=='-':
            begin=1
            sign=1
        else:
            return 0


        for i in range(begin,len(str)):
            if str[i].isdigit():
                result*=10;
                result+=int(str[i])
            else:
                break
        if result>2147483647 and sign==0:
            return 2147483647
        elif result>2147483648 and sign==1:
            return -2147483648
        else:
            return -result if sign else result


sol=Solution()
print sol.myAtoi("1")