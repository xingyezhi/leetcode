__author__ = 'xingyezhi'
# encoding: utf-8
class Solution(object):
    def minDistance(self, word1, word2):
        if len(word1)==0 or len(word2)==0:return max(len(word1),len(word2))
        map=[[0]*(len(word2)+1) for i in range((len(word1)+1))]
        for i in range(len(word1)):
            map[i+1][0]=i+1
        for j in range(len(word2)):
            map[0][j+1]=j+1
        for i in range(0,len(word1)):
            for j in range(0,len(word2)):
                if word1[i]==word2[j]:
                    map[i+1][j+1]=min(map[i][j],map[i+1][j]+1,map[i][j+1]+1)
                else:
                    map[i+1][j+1]=min(map[i+1][j],map[i][j+1],map[i][j])+1
        #print map
        return map[len(word1)][len(word2)]

sol=Solution()
print sol.minDistance("a","ab")