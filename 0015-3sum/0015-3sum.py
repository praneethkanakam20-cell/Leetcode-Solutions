class Solution(object):
    def threeSum(self, a):
        li=[]
        a.sort()
        for i in range(len(a)-2):
            s=0
            if i>0 and a[i]==a[i-1]:
                continue
            l=i+1
            r=len(a)-1
            while l<r:
                s=a[i]+a[l]+a[r]
                if s==0:
                    li.append([a[i],a[l],a[r]])
                    l+=1
                    r-=1
                    while l<r and a[l]==a[l-1]:
                        l+=1
                    while l<r and a[r]==a[r+1]:
                        r-=1
                elif s<0:
                    l+=1
                else:
                    r-=1
        return li