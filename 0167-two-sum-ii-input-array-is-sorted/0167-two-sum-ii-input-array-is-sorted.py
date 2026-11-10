class Solution(object):
    def twoSum(self, num, target):
        l=0
        r=len(num)-1
        s=0
        while l<=r:
            s=num[l]+num[r]
            if s==target:
                return [l+1,r+1]
            elif s>target:
                r-=1
            elif s<target:
                l+=1
        