#naive approach
#time limit exceeded.
#tc: O(n^2)
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         rectangle = []

#         for i in range(len(heights)):
#             left_count, right_count = 0, 0

#             left_pointer, right_pointer = i, i 

#             #loop left
#             while left_pointer - 1 >= 0 and heights[left_pointer - 1] >= heights[i]:
#                 left_count += 1
#                 left_pointer -= 1

#             #loop right
#             while right_pointer + 1 <= len(heights) - 1 and heights[right_pointer + 1] >= heights[i]:
#                 right_count += 1
#                 right_pointer += 1
#             rectangle.append((left_count + right_count + 1) * heights[i])
#         return max(rectangle)

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # Pairs of (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            # If the current bar is shorter than the bar at the top of the stack,
            # we can no longer extend that taller bar's rectangle. We must pop it
            # and calculate its area.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                # The popped bar's rectangle could have started as far back as its own index
                start = index
            
            stack.append((start, h))
        
        # After the loop, calculate area for any remaining bars in the stack
        # These bars can extend all the way to the end of the histogram
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
            
        return max_area



