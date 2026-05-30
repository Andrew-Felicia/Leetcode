class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] S = s.toCharArray();
        int n = S.length;
        int ans = 0;
        int left = 0;
        int[] record = new int[128];

        for (int right = 0; right < n; right++) {
            char c = S[right];
            record[c] += 1; //it will convert char to ascii atomatically.
            while(record[c] > 1) {
                record[S[left]] -= 1;
                left ++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;

        
    }
}