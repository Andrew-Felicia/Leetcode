from typing import List




#t:75ms
#s:29.25MB
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         if n <= 1:
#             raise IllegalArgumentError("height must contain at least two values!")

#         start = 0
#         end = n - 1

#         ContainedWater = min(height[start], height[end]) * (end - start)

#         while start != end and start <= n -2 and end >= 1:
#             if height[start] <= height[end]:
#                 start += 1
#                 if min(height[start], height[end]) * (end - start) > ContainedWater:
#                     ContainedWater = min(height[start], height[end]) * (end - start)
#             if height[start] > height[end]:
#                 end -= 1
#                 if min(height[start], height[end]) * (end - start) > ContainedWater:
#                     ContainedWater = min(height[start], height[end]) * (end - start)
#         return ContainedWater

#t:83ms
#s:29MB
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         if n <= 1:
#             raise IllegalArgumentError("height must contain at least two values!")

#         start = 0
#         end = n - 1

#         ContainedWater = min(height[start], height[end]) * (end - start)

#         while start != end and start <= n -2 and end >= 1:
#             if height[start] <= height[end]:
#                 start += 1
#                 new_water = min(height[start], height[end]) * (end - start)
#                 if  new_water > ContainedWater:
#                     ContainedWater = new_water
#             if height[start] > height[end]:
#                 end -= 1
#                 new_water = min(height[start], height[end]) * (end - start)
#                 if new_water > ContainedWater:
#                     ContainedWater = new_water
#         return ContainedWater



class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            raise ValueError("height must contain at least two values!")

        start = 0
        end = n - 1

        ContainedWater = min(height[start], height[end]) * (end - start)

        while start != end and start <= n -2 and end >= 1:
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
            new_water = min(height[start], height[end]) * (end - start)
            if new_water > ContainedWater:
                ContainedWater = new_water
        return ContainedWater
    