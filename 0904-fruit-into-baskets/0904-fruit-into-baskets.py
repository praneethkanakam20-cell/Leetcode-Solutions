class Solution(object):
    def totalFruit(self, a):
        f={}
        l,m=0,0
        for r in range(len(a)):
            f[a[r]]=f.get(a[r],0)+1
            if len(f)>2:
                f[a[l]]-=1
                if f[a[l]]==0:
                    del f[a[l]]
                l+=1
            if len(f)<=2:
                m=max(m,r-l+1)
        return m