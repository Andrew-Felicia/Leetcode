import java.util.HashMap;
import java.util.Map;

class Solution {
    public int longestPalindrome(String s) {
        if (s.length() == 1) {
            return 1;
        }
        
        Map<Character, Integer> frequency = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char character = s.charAt(i);
            frequency.compute(character, (k, v) -> (v == null) ? 1 : v + 1);
        }

        int ans = 0;
        boolean hasOddNumber = false;
        for (Map.Entry<Character, Integer> entry : frequency.entrySet()) {
            int count = entry.getValue();

            ans += (count / 2) * 2;

            if (count % 2 != 0) {
                hasOddNumber = true;
            }
        }
        if (hasOddNumber) {
            ans ++;
        }

        return ans;
        
    }
}