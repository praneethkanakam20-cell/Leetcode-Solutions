class Solution(object):
    def asteroidCollision(self, a):
        l=[]
        y=True
        for x in a:
            y=True
            while y and l and x<0 and l[-1]>0:
                if l[-1]<-x:
                    l.pop()
                elif l[-1]==-x:
                    l.pop()
                    y=False
                else:
                    y=False
            if y:
                l.append(x)
        return l