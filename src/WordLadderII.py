__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def bfs(self,wordList,beginWord,endWord):
        q=[beginWord]
        flag,visit=False,{}
        visit[beginWord],visit[endWord]=None,[]
        while len(q)!=0:
            temp=[]
            for s in q:
                for i in range(len(s)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        s2=s[:i]+j+s[i+1:]
                        if s2==endWord:
                            visit[s2].append(s)
                            flag=True
                        if s2 not in wordList:
                            continue
                        if not visit.has_key(s2):
                            visit[s2]=[s]
                            temp.append(s2)
                        elif s2 in temp:
                            visit[s2].append(s)
                wordList.remove(s)
            q=temp
            if flag:break
        return self.build_result(visit,endWord)
    def build_result(self,visit,endWord):
        result=[]
        if visit[endWord]!=None:
            for i in visit[endWord]:
                sub=self.build_result(visit,i)
                for j in sub:
                    j.append(endWord)
                result.extend(sub)
            return result
        else:
            return [[endWord]]
    def findLadders(self, beginWord, endWord, wordList):
        wordList.add(beginWord)
        return self.bfs(wordList,beginWord,endWord)
sol=Solution()
print sol.findLadders("a",
"c",
set(["a","b","c"]))
