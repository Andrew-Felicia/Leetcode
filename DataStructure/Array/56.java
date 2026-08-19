import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.List;

// class Solution {
//     public int[][] merge(int[][] intervals) {
//         Arrays.sort(intervals, (p, q) -> p[0] - q[0]);
//         List<List<Integer>> ans = new ArrayList<>();

//         for(int[] i : intervals) {
//             if(ans.isEmpty() || ans.get(ans.size() - 1).get(1) < i[0]) {
//                 ans.add(Arrays.stream(i).boxed().collect(Collectors.toList())); 
//                 //convert int[] to ArrayList
//             } else {
//                 int current = ans.get(ans.size() - 1).get(1);
//                 ans.get(ans.size() - 1).set(1, Math.max(i[1], current));
//             }

//         }
//         // Convert List<List<Integer>> back to int[][]
//         return ans.stream()
//                   .map(list -> list.stream().mapToInt(Integer::intValue).toArray())
//                   .toArray(int[][]::new);
//     }
// }



class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (p, q) -> Integer.compare(p[0], q[0]));
        int[][] ans = new int[intervals.length][2];
        
        //index indicates how many elements inside ans.
        int index = 0;
        for(int[] i : intervals) {
            if(index == 0 || ans[index - 1][1] < i[0]) {
                ans[index] = i;
                index += 1;
            } else {
                ans[index - 1][1] = Math.max(ans[index - 1][1], i[1]);
            }
        }

        //ans may not be full.
        return Arrays.copyOfRange(ans, 0, index);
    }


}

// class Solution {
//     public int[][] merge(int[][] intervals) {
//         Arrays.sort(intervals, (p, q) -> Integer.compare(p[0], q[0]));

//         List<int[]> ans = new ArrayList<>();
//         for(int[] i : intervals) {
//             if(ans.isEmpty() || ans.get(ans.size() - 1)[1] < i[0]) {
//                 ans.add(i);
//             } else {
//                 int current = ans.get(ans.size() - 1)[1];
//                 ans.get(ans.size() - 1)[1] = Math.max(i[1], current);
//             }
//         }
//         // Convert the dynamic List<int[]> back to a primitive 2D array effortlessly
//         return ans.toArray(new int[ans.size()][]);
//     }

// }