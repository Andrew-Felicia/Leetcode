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
    public ListNode middleNode(ListNode head) {
        ListNode cur = head;
        int counts = 0;
        while (cur != null) {
            counts++;
            cur = cur.next;
        }
        int mid = counts / 2;

        cur = head;
        while (mid > 0) {
            cur = cur.next;
            mid -= 1;
        }
        return cur;
    }
}