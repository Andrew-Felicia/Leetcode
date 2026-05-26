class Solution {
    public int longestConsecutive(int[] nums) {
        //convert nums to set.
        Set<Integer> nums_set = new HashSet<>();
        for(int i : nums) {
            nums_set.add(i);
        }

        int ans = 0;

        for(int num : nums_set) {
            //find the minimum element of one of the consecutive sequences.
            if(nums_set.contains(num -1)) continue;

            int y = num + 1;
            while(nums_set.contains(y)) {
                y += 1;
            }
            ans = Math.max(ans, y - num);

        }
        return ans;
    }
}