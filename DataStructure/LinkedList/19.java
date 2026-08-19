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
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head.next == null && n == 1) {
            return null;
        }

        ListNode tmp = head;
        int counts = 0;
        while(tmp != null) {
            tmp = tmp.next;
            counts += 1;
        }

        int left = counts - n;
        if(left == 0) return head.next;

        tmp = head;
        for(int i = 0; i < left - 1; i++) {
            tmp = tmp.next;
        }
        ListNode tmp1 = tmp.next.next;
        tmp.next = tmp1;

        return head;
    }
}