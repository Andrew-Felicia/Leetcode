from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. Sort the array: Essential for Two-Pointers and skipping duplicates.
        nums.sort()
        n = len(nums)
        result = []

        # The main recursive function is tailored for the '3' sum
        def find_triplets(start_index: int):
            
            # The base case or main loop for the first element 'a'
            for i in range(start_index, n - 2):
                
                # Skip duplicates for the first number 'a'
                # If the current number is the same as the previous one, skip it.
                if i > start_index and nums[i] == nums[i - 1]:
                    continue
                
                # Target for the remaining two numbers: target = -nums[i]
                target = -nums[i]
                
                # Call the Two-Pointer helper function
                # This finds 'b' and 'c' such that b + c = target
                two_sum_pointers(i + 1, target, nums[i])
        
        # Helper function using the Two-Pointer technique (iterative for efficiency)
        # This is where the core O(n) work happens for each 'a'
        def two_sum_pointers(left: int, target: int, first_num: int):
            right = n - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    # Found a triplet!
                    result.append([first_num, nums[left], nums[right]])
                    
                    # Move pointers and skip duplicates for 'b' and 'c'
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the second number 'b'
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # Skip duplicates for the third number 'c'
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum < target:
                    # Sum is too small, need a larger 'b', move left pointer right
                    left += 1
                else: # current_sum > target
                    # Sum is too large, need a smaller 'c', move right pointer left
                    right -= 1

        # Start the recursion/loop from index 0
        find_triplets(0)
        return result