class Solution(object):
    def longestOnes(self, a, k):
        l,z,m=0,0,0
        for r in range(len(a)):
            if a[r]==0:
                z+=1
            if z>k:
                if a[l]==0:
                    z-=1
                l+=1
            if z<=k:
                m=max(m,r-l+1)
        return m