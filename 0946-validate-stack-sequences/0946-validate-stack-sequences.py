class Solution(object):
    def validateStackSequences(self, pushed, popped):
        s=[]
        for i in range(len(pushed)):
            s.append(pushed[i])
            j=0
            while s and len(popped)>=0:
                if s[-1]==popped[0]:
                    s.pop()
                    popped.remove(popped[0])
                    j+=1
                else:
                    break
        return len(s)==0