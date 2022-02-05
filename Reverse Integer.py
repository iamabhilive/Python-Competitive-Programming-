class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)[::-1].lstrip('0').rstrip('-')
        if x == 0 or int(a) < -2**31 or int(a) > 2**31-1:
            return 0
        elif x < 0:
            return '-' + a
        else:
            return a
