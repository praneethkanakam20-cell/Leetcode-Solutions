class Solution(object):
    def threeSumClosest(self, n, t):
        n.sort()
        m=float("inf")
        s2=0
        for i in range(len(n)-2):
            s=0
            if i>0 and n[i-1]==n[i]:
                continue
            l=i+1
            r=len(n)-1
            while l<r:
                s=n[i]+n[l]+n[r]
                c=abs(t-s)
                if c<m:
                    m=c
                    s2=s
                elif s<t:
                    l+=1
                    while l<r and n[l]==n[l-1]:
                        l+=1
                elif s>t:
                    r-=1
                    while l<r and n[r]==n[r+1]:
                        r-=1
                else:
                    return s
        return s2