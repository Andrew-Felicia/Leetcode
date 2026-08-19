class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] cnt_p = new int[26];
        for(char c : p.toCharArray()) {
            cnt_p[c - 'a']++;
        }

        List<Integer> ans = new ArrayList<>();
        int[] cnt_window = new int[26];
        for(int right = 0; right < s.length(); right++) {
            cnt_window[s.charAt(right) - 'a'] += 1;
            int left = right - p.length() + 1;

            if(left < 0) continue;

            if(Arrays.equals(cnt_p, cnt_window)) {
                ans.add(left);
            }
            cnt_window[s.charAt(left) - 'a'] -= 1;
        }
        return ans;
    }
}