/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

import java.util.HashSet;
import java.util.Set;

class Solution {
    public ListNode removeDuplicateNodes(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;
        Set<Integer> buffer = new HashSet<>();

        while (cur != null) {
            if (buffer.contains(cur.val)) {
                prev.next = cur.next;
            } else {
                buffer.add(cur.val);
                prev = cur;
            }
            cur = cur.next;
        }
        return head;
    }
}