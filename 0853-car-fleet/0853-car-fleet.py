class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        l=[]
        for pos,sp in cars:
            time=(target-pos)/sp
            if not l or time>l[-1]:
                l.append(time)
        return len(l)