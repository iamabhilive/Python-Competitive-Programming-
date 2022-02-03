class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        l = []
        a = 0
        for i in num:
            a = a * 10 + int(i)
        a += k
        for i in str(a):
            l.append(int(i))
            
        return l
