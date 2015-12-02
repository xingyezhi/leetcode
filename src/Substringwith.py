__author__ = 'lenovo'
# coding=utf-8
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        size=len(words)
        if size==0:
            return range(len(s))
        length=len(words[0])
        if len(s)<length:
            return []
        strmap={}
        for i in words:
            strmap.setdefault(i,0)
            strmap[i]+=1
        result=[]
        for i in range(length):
            j=i
            begin=i
            submap=dict(strmap)
            dicmap={}
            counts=0
            while j<len(s):
                substr=s[j:j+length]
                if not submap.has_key(substr):
                    submap=dict(strmap)
                    dicmap={}
                    counts=0
                    j+=length
                    begin=j
                elif submap[substr]>0:
                    dicmap.setdefault(substr,[])
                    dicmap[substr].append(j)
                    j+=length
                    counts+=1
                    submap[substr]-=1
                    if counts==size:
                        result.append(begin)
                        strs=s[begin:begin+length]
                        submap[strs]+=1
                        dicmap[strs].pop(0)
                        counts-=1
                        begin+=length
                else:
                    j+=length
                    end=dicmap[substr][0]+length
                    k=begin
                    begin=end
                    while k<end:
                        strs=s[k:k+length]
                        k+=length
                        submap[strs]+=1
                        dicmap[strs].pop(0)
                        counts-=1
                    submap[substr]-=1
                    counts+=1
                    dicmap.setdefault(substr,[])
                    dicmap[substr].append(j-length)
        return result

sol=Solution()
print sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])






