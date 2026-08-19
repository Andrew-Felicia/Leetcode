class Solution {
    public String minWindow(String s, String t) {
        int[] cntT = new int[128];
        int[] cntS = new int[128];
         for(char i : t.toCharArray()) {
            cntT[i] += 1;
        }
        
        int m = s.length();
        char[] S = s.toCharArray();
        int left = 0;
        int ansLeft = -1;
        int ansRight = m;

        for(int right = 0; right < m; right++) {
            cntS[S[right]] += 1;
            while(isCovered(cntT, cntS)) {
                if(right - left < ansRight - ansLeft) {
                    ansLeft = left;
                    ansRight = right;
                }
                cntS[S[left]] -= 1;
                left += 1;
            }
        }

        return ansLeft < 0? "" : s.substring(ansLeft, ansRight + 1);


    }

    private boolean isCovered(int[] cntT, int[] cntS) {
        for(char i = 'A'; i <= 'Z'; i++) {
            if(cntS[i] < cntT[i]) return false;
        }

        for(char i = 'a'; i <= 'z'; i++) {
            if(cntS[i] < cntT[i]) return false;
        }

        return true;
    }
}