__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def __init__(self):
        self.result=[]
    def midper(self,nums,cur):
        if cur==len(nums)-1:
            self.result.append(nums[:])
            return
        else:
            for i in range(cur,len(nums)):
                if i!=cur and nums[cur]==nums[i]:
                    continue
                nums[cur],nums[i]=nums[i],nums[cur]
              #  print nums
                self.midper(nums,cur+1)
                nums[cur],nums[i]=nums[i],nums[cur]
                #nums[cur],nums[i]=nums[i],nums[cur]
    def permute(self, nums):
        self.midper(nums,0)
        return self.result


sol=Solution()
print sol.permute([1,1,3])


# class Solution {
# public:
#     void recursion(vector<int> num, int i, int j, vector<vector<int> > &res) {
#         if (i == j-1) {
#             res.push_back(num);
#             return;
#         }
#         for (int k = i; k < j; k++) {
#             if (i != k && num[i] == num[k]) continue;
#             swap(num[i], num[k]);
#             recursion(num, i+1, j, res);
#         }
#     }
#     vector<vector<int> > permuteUnique(vector<int> &num) {
#         sort(num.begin(), num.end());
#         vector<vector<int> >res;
#         recursion(num, 0, num.size(), res);
#         return res;
#     }
# };


