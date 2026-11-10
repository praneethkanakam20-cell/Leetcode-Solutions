class Solution(object):
    def maxScore(self, card, k):
        r=len(card)-1
        s,m=0,0
        for i in range(k):
            s+=card[i]
        m=max(m,s)
        for i in range(k-1,-1,-1):
            s=s-card[i]+card[r]
            m=max(m,s)
            r-=1
        return m