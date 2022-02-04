class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = True
        for i in s:
            if s.count(i) > 1:
                continue
            else:
                f = False
                return s.index(i)
                break
        if f:
            return -1
