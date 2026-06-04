// class Solution {
//     public int maxSubArray(int[] nums) {
//         int n = nums.length;
//         List<Integer> dp = new ArrayList<>(n + 1);
//         //n Java, writing new ArrayList<>(n + 1) only allocates capacity (internal memory space); 
//         //it does not actually fill the list with elements. The list size is still 0.
//         int ans = 0;
//         //dp[0] = nums[0];
//         dp.set(0, nums[0]);

//         for(int i = 1; i < n; i++) {
//             dp.set(i, Math.max(nums[i], dp.get(i - 1) + nums[i]));
//             ans = Math.max(ans, dp.get(i));
//         }

//         return ans;
//     }
// }

class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n + 1];
        int ans = nums[0];
        dp[0] = nums[0];

        for(int i = 1; i < n; i++) {
            dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
            ans = Math.max(ans, dp[i]);
        }

        return ans;



    }

}