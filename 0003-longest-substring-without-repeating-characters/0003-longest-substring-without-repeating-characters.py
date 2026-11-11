class Solution(object):
    def lengthOfLongestSubstring(self, s):
        h={}
        l=0
        m=0
        for r in range(len(s)):
            if s[r] in h and h[s[r]]>=l:
                l=h[s[r]]+1
            h[s[r]]=r
            m=max(m,r-l+1)
        return m