class Solution {
    Map<String, String[]> words = Map.of(
                "2", new String[]{"a", "b", "c"},
                "3", new String[]{"d", "e", "f"},
                "4", new String[]{"g", "h", "i"},
                "5", new String[]{"j", "k", "l"},
                "6", new String[]{"m", "n", "o"},
                "7", new String[]{"p", "q", "r", "s"},
                "8", new String[]{"t", "u", "v"},
                "9", new String[]{"w", "x", "y", "z"}
            );
    public List<String> letterCombinations(String digits) {
        if(digits.length() == 0) {
            return new ArrayList<>();
        } 
        if(digits.length() == 1) {
            List<String> result = new ArrayList<>();
            for(String s : words.get(digits)) {
                result.add(s);
            }
            return result;
        } 
        List<String> result = new ArrayList<>();
        String first = digits.substring(0, 1);
        String remain = digits.substring(1);
        for(String s : words.get(first)) {
            for(String s1 : letterCombinations(remain)) {
                result.add(s + s1);
            }
        }
        return result;
    }
}