class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 1:
            return 1
        else:
            c = 0
            for i in b:
                c = 10 * c + i
            return pow(a, c, 1337)
