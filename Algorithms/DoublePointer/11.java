// class Solution {
//     public int maxArea(int[] height) {
//         int left = 0;
//         int right = height.length - 1;
//         int ans = Math.min(height[left], height[right]) * (right - left);

//         while(left <= height.length - 2 && right >= 1 && left < right) {
//             if(height[left] <= height[right]) {
//                 left += 1;
//                 ans = Math.max(ans, Math.min(height[left], height[right]) * (right - left));
//             } else {
//                 right -= 1;
//                 ans = Math.max(ans, Math.min(height[left], height[right]) * (right - left));
//             }

//         }
//         return ans;

//     }
// }

class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int ans = 0;

        while(left <= height.length - 2 && right >= 1 && left < right) {
            int area = Math.min(height[left], height[right]) * (right - left);
            ans = Math.max(ans, area);
            if(height[left] <= height[right]) {
                left += 1;
            } else {
                right -= 1;
            }

        }
        return ans;

    }
}