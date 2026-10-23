import re
class Solution:
    def calculate(self, s: str) -> int:
        l=[]
        n=0
        r=0
        x=1
        for i in s:
            if i.isdigit():
                n=n*10+int(i)
            elif i=="+":
                r+=x*n
                n=0
                x=1
            elif i=="-":
                r+=x*n
                n=0
                x=-1
            elif i=="(":
                l.append(r)
                l.append(x)
                r=0
                x=1
            elif i==")":
                r+=n*x
                n=0
                r*=l.pop()
                r+=l.pop()
        r+=n*x
        return r