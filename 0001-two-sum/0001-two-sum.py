class Solution(object):
    def twoSum(self, nums, target):
        a=len(nums)
        for i in range(0,a):
            for j in range(1,a):
                if i!=j :
                    if (nums[i]+nums[j])==target :
                        return [i,j]
        