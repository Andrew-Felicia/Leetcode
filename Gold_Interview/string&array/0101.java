import java.util.Set;
import java.util.HashSet;
import java.util.stream.Collectors;

class Solution {
    public boolean isUnique(String astr) {
        Set<Character> set = astr.chars()
                                 .mapToObj(c -> (char) c)
                                 .collect(Collectors.toSet());
        return set.size() == astr.length();
    }
}