class Solution:
    def evalRPN(self, t: list[str]) -> int:
        l = []
        r = 0
        for x in t:
            if x not in ["+", "-", "/", "*"]:
                l.append(int(x))
            else:
                b = l.pop()
                a = l.pop()
                if x == "+":
                    r = a + b
                elif x == "-":
                    r = a - b
                elif x == "*":
                    r = a * b
                else:
                    r=int(a/b)
                l.append(r)
        return l[-1]