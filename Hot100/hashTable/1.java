//O(n^2)
// class Solution {
//     public int[] twoSum(int[] nums, int target) {
//         for(int i = 0; i < nums.length - 1; i++) {
//             for(int j = i + 1; j < nums.length; j++) {
//                 if(nums[i] + nums[j] == target) {
//                     return new int[]{i, j};
//                 }

//             }
//         }
        
//         return new int[]{};
//     }
// }

import java.util.HashMap;
import java.util.Map;
//O(n)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> result = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            if(result.containsKey(target - nums[i])) {
                return new int[]{i, result.get(target - nums[i])};
            }

            result.put(nums[i], i);
        }
        
        return new int[]{};
    }
}