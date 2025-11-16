class Solution:
    def numSub(self, s: str) -> int:
        n = 0
        temp = 0
        for digit in s:
            if digit == '1':
                temp += 1
                n += temp
            else:
                temp = 0
        return (n % (10**9 + 7))