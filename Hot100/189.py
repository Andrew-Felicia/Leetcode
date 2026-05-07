from typing import List

#timeout
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if k == 0 or len(nums) == 1:
#             return
#         for _ in range(k):
#             self.rotateOnce(nums)
        
#     def rotateOnce(self, nums: List[int]) -> None:
#         last = nums[-1]
#         nums[1:] = nums[0:-1]
#         nums[0] = last



#nums is a list passed by reference.
#nums = tmp2 + tmp1, does not modify the original list in-place. Instead, it rebinds the local variable nums to a new list.

# This means that outside this function, the original list is unchanged. The caller sees no effect.
def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        times = k % len(nums)
        if k == 0 or len(nums) == 1 or times == 0:
            return
        tmp1 = nums[0:len(nums) - times] #first part
        tmp2 = nums[len(nums) - times:] #second part
        nums = tmp2 + tmp1 

#Here, you are modifying slices of nums in-place:
# nums[0:times] = tmp2
# nums[times:] = tmp1
#This actually changes the contents of the original list, which is exactly what the problem asks for (modify nums in-place).

def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        times = k % len(nums)
        if k == 0 or len(nums) == 1 or times == 0:
            return
        
        tmp1 = nums[0:len(nums) - times] #first part
        tmp2 = nums[len(nums) - times:] #second part
        nums[0:times] = tmp2
        nums[times:] = tmp1

nums = [1,2,3,4,5,6,7] #-> [5,6,7,1,2,3,4], k==3
 #-> [7,1,2,3,4,5,6], k==1

rotate(nums, 15)
print(nums)