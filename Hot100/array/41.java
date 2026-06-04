// class Solution {
//     public int firstMissingPositive(int[] nums) {
//         List<Integer> positive = new ArrayList<>();
//         for(int i : nums) {
//             if(i > 0) {
//                 positive.add(i);
//             }
//         }

//         if(positive.isEmpty()) return 1;

//         int maxValue = Collections.max(positive);
//         for(int i = 1; i < maxValue; i++) {
//             if(!positive.contains(i)) return i; //time limit exceeded, because this method is O(n^2);
//         }

//         return maxValue + 1;
//     }
// }



class Solution {
    public int firstMissingPositive(int[] nums) {
        List<Integer> positive = new ArrayList<>();
        for(int i : nums) {
            if(i > 0) {
                positive.add(i);
            }
        }
        Set<Integer> positive_set = new HashSet<>(positive);
        if(positive_set.isEmpty()) return 1;

        int maxValue = Collections.max(positive);
        for(int i = 1; i < maxValue; i++) {
            if(!positive_set.contains(i)) return i; //passed the test. because set inquery is O(1).
        }

        return maxValue + 1;
    }
}