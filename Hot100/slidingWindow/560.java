class Solution {
    public int subarraySum(int[] nums, int k) {
        int ans = 0;
        int n = nums.length;
        int[] preSum = new int[n + 1];
        for(int i = 0; i < n; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
        }

        Map<Integer, Integer> preSum_recorder = new HashMap<>(n + 1);
        for(int i : preSum) {
            ans += preSum_recorder.getOrDefault(i - k, 0);
            preSum_recorder.merge(i, 1, Integer::sum);

        }
        return ans;
    }
}