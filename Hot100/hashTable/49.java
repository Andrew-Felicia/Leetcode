import java.util.HashMap;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();
        for(String s : strs) {
            char[] sorted_s = s.toCharArray(); //caution: not s.tocharArray().
            Arrays.sort(sorted_s);

            result.computeIfAbsent(new String(sorted_s), _ -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(result.values());
    }
}