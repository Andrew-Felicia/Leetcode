# class Solution:
#     @cache
#     def tribonacci(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         elif n == 2:
#             return 1
#         else:
#             return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        
        

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        p, q, r = 0, 1, 1
        for _ in range(n - 2):
            p, q, r = q, r, p + q + r
        return r

        