__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def candy(self, ratings):
        ratings.append(1<<32-1)
        result=i=front=0
        while i<(len(ratings)-1):
            if ratings[i]<=ratings[i+1]:
                front+=1
                result+=front
                if ratings[i]==ratings[i+1]:
                    front=0
            else:
                end,front2=i,0
                while end<(len(ratings)-1):
                    if ratings[end]<=ratings[end+1]:
                        break
                    front2+=1
                    result+=front2
                    end+=1
                result+=max(front,front2)+1
                if ratings[end]==ratings[end+1]:
                    i,front=end,0
                else:
                    i,front=end,1
            i+=1
        return result

# 20001
# 38490
sol=Solution()
print sol.candy([4,2,3,4,1])



