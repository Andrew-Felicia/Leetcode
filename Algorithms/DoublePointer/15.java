class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        int nums_length = nums.length;

        for(int i = 0; i < nums_length - 2; i++) {
            if(nums[i] > 0) {
                return result;
            }
            //skip the duplicate first element.
            if(i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = nums_length - 1;

            while(left < right) {
                int threeNumsSum = nums[i] + nums[left] + nums[right];
                if(threeNumsSum < 0) {
                    left += 1;
                } else if(threeNumsSum > 0) {
                    right -= 1;
                } else {
                    //result.add([nums[i],nums[left],nums[right]]); won't compile
                    result.add(new ArrayList<>(List.of(nums[i],nums[left],nums[right])));
                    left += 1;
                    right -= 1;


                    while(left < right && nums[left] == nums[left - 1]) {
                        left += 1;
                    }

                    while(left < right && nums[right] == nums[right + 1]) {
                        right -= 1;
                    }
                }
            }


        }
        return result;
    }
}