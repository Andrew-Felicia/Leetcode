class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        Deque<Integer> recorder = new ArrayDeque<>();
        int[] ans = new int[n - k + 1];

        for(int i = 0; i < n; i++) {
            while(!recorder.isEmpty() && nums[recorder.getLast()] <= nums[i]) {
                recorder.removeLast();
            }

            recorder.addLast(i);

            int left = i - k + 1;
            if(recorder.getFirst() < left) {
                recorder.removeFirst();
            }

            if(left >= 0) {
                ans[left] = nums[recorder.getFirst()];
            }
        }

        return ans;
    }
}