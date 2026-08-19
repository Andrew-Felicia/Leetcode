class Trie {

    private static class TrieNode {
        TrieNode[] son = new TrieNode[26];
        boolean end = false;
    }

    private final TrieNode root = new TrieNode();
    
    public void insert(String word) {
        TrieNode cur = root;
        for(char c : word.toCharArray()) {
            c -= 'a';
            if(cur.son[c] == null) {
                cur.son[c] = new TrieNode();
            }
            cur = cur.son[c];
        }
        cur.end = true;
    }
    
    public boolean search(String word) {
        TrieNode cur = root;
        for(char c : word.toCharArray()) {
            c -= 'a';
            if(cur.son[c] == null) {
                return false;
            }
            cur = cur.son[c];
        }
        return cur.end;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode cur = root;
        for(char c : prefix.toCharArray()) {
            c -= 'a';
            if(cur.son[c] == null) {
                return false;
            }
            cur = cur.son[c];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */