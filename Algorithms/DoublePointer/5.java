class Solution {
    public String longestPalindrome(String s) {
        int left = 0;
        int right = 0;

        //odd palindrome.
        for (int i = 0; i < s.length(); i++) {
            int l = i;
            int r = i;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                l -= 1;
                r += 1;
            }
            if (r - l - 1 > right - left) {
                left = l + 1;
                right = r;
            }
        }

        //even palendrome
        for (int i = 0; i < s.length(); i++) {
            int l = i;
            int r = i + 1;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                l -= 1;
                r += 1;
            }
            if (r - l - 1 > right - left) {
                left = l + 1;
                right = r;
            }
        }

        return s.substring(left, right);
    }
}