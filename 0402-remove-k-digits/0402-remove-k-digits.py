class Solution(object):
    def removeKdigits(self, num, k):
        l=[]
        a=""
        for x in num:
            while k>0 and l and l[-1]>x:
                b=l.pop()
                k=k-1
            l.append(x)
        while k>0:
            l.pop()
            k-=1
        a="".join(l)
        a=a.lstrip("0")
        if a=="":
            return "0"
        else:
            return a