class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        if(nums.length == 1) {
            List<Integer> tmp = new ArrayList<>();
            List<Integer> tmp1 = new ArrayList<>();
            List<List<Integer>> result = new ArrayList<>();
            result.add(tmp);
            tmp1.add(nums[0]);
            result.add(tmp1);
            return result;
        } else {
            int first = nums[0];
            int[] remain = Arrays.copyOfRange(nums, 1, nums.length);
            List<List<Integer>> result = subsets(remain);
            for(List<Integer> tmp : subsets(remain)) {
                tmp.add(first);
                result.add(tmp);
            }
            return result;

        }
    }
}