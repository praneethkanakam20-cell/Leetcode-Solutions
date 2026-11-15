class Solution(object):
    def maximizeSum(self, nums, k):
        nums.sort()
        s=0
        for i in range(k):
            s+=nums[-1]
            nums[-1]=nums[-1]+1
        return s