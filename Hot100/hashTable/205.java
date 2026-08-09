import java.util.Arrays;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] sTot = new int[128];
        int[] tTos = new int[128];

        Arrays.fill(sTot, -1);
        Arrays.fill(tTos, -1);

        for (int i = 0; i < s.length(); i++) {
            char source = s.charAt(i);
            char target = t.charAt(i);

            if (sTot[source] == -1 && tTos[target] == -1) {
                sTot[source] = target;
                tTos[target] = source;
            } else if (sTot[source] != target || tTos[target] != source) {
                return false;
            }

        }
        return true;
    }
}