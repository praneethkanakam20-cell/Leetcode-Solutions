class Solution(object):
    def lengthOfLongestSubstring(self, s):
        m=0
        i=0
        for j in range(len(s)):
            while len(s[i:j+1])!=len(set(s[i:j+1])):
                i+=1
            m=max(len(s[i:j+1]),m)
        return m