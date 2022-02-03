class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = []
        a = 0
        for i in digits:
            a = a * 10 + i
        a += 1
        for i in str(a):
            l.append(int(i))
            
        return l
