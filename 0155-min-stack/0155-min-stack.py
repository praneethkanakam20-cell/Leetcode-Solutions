class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        self.a=0

    def push(self, value):
        self.stack.append(value)
        if self.min_stack :
            if value<=self.min_stack[-1]:
                self.min_stack.append(value)
        else:
            self.min_stack.append(value)

    def pop(self):
        self.a=self.stack.pop()
        if self.min_stack[-1]==self.a:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()