class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if(nums.length == 0) {
            return result;
        } else if(nums.length == 1) {
            List<Integer> tmp = new ArrayList<>();
            tmp.add(nums[0]);
            result.add(tmp);
            return result;
        } else {
            for(int i = 0; i < nums.length; i++) {
                int current = nums[i];
                int[] remaining = new int[nums.length - 1];
                int idx = 0;
                for(int j = 0; j < nums.length; j++) {
                    if(i == j) continue;
                    remaining[idx++] = nums[j];
                }

                List<List<Integer>> sub = permute(remaining);
                for(List<Integer> perm : sub) {
                    List<Integer> newList = new ArrayList<>();
                    newList.add(current);
                    newList.addAll(perm);
                    result.add(newList);
                }
            }
            return result;
        }

    }
}