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
    public ListNode reverseKGroup(ListNode head, int k) {
        //count how many nodes;
        int counts = 0;
        for(ListNode cur = head; cur != null; cur = cur.next) {
            counts += 1;
        }

        ListNode dummy = new ListNode(5, head);
        ListNode p0 = dummy;
        ListNode prev = null;
        ListNode cur = head;

        for(int i = 0; i < counts / k; i++) {
            for(int j = 0; j < k; j++) {
                ListNode nxt = cur.next;
                cur.next = prev;
                prev = cur;
                cur = nxt;
            }
            
            ListNode tmp = p0.next;
            p0.next.next = cur;
            p0.next = prev;
            p0 = tmp;
        }

        return dummy.next;

    }
}