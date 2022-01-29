class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1
        middle = 0
        while left < right:
            middle = (left + right - 1) // 2
            middle_square = middle * middle

            if middle_square < x:
                left = middle + 1
            elif middle_square > x:
                right = middle
            else:
                return middle
        if middle * middle > x:
            return middle - 1
        if middle * middle < x:
            return middle
