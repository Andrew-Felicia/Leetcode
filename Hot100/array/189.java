class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        int remain = k % n;
        if(k == 0 || n == 1 || remain == 0) {
            return;
        }
        
        //reverse the whole array;
        reverse(nums, 0, n - 1);

        reverse(nums, 0, remain - 1);

        reverse(nums, remain, n - 1);

    }

    private void reverse(int[] nums, int start, int end) {
        while(start < end) {
            int tmp = nums[start];
            nums[start] = nums[end];
            nums[end] = tmp;
            start += 1;
            end -= 1;
        }
    }
}