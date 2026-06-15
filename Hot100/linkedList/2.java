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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(5); // dummy node;
        ListNode cur = result;
        int carry = 0;

        while(l1 != null || l2 != null || carry != 0) {
            int val_1 = (l1 == null) ? 0 : l1.val;
            int val_2 = (l2 == null) ? 0 : l2.val;


            int digit = (val_1 + val_2 + carry) % 10;
            carry = (val_1 + val_2 + carry) / 10;

            cur.next = new ListNode(digit);
            cur = cur.next;

            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
        }

        return result.next;
    }
}