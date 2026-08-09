class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.length() > t.length()) {
            return false;
        }
        if (s.length() == 0) {
            return true;
        }

        int sp = 0;
        int tp = 0;
        while (tp < t.length()) {
            if (s.charAt(sp) == t.charAt(tp)) {
                sp++;
            }
            tp++;
            if (sp == s.length()) {
                return true;
            }
        }


        return false;
    }
}