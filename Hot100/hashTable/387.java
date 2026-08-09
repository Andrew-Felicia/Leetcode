class Solution {
    public int firstUniqChar(String s) {
        int[] frequency = new int[26];
        for (int i = 0; i < s.length(); i++) {
            char character = s.charAt(i);
            int index = character - 'a';
            frequency[index] += 1; 
        }

        for (int i = 0; i < s.length(); i++) {
            char character = s.charAt(i);
            int index = character - 'a';
            if (frequency[index] == 1) {
                return i;
            }
        }
        return -1;
    }
}