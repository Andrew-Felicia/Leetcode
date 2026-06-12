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
    private ListNode reverseLinkedList(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;
        while(cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }
    
    private ListNode findMiddle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }

    public boolean isPalindrome(ListNode head) {
        ListNode mid = findMiddle(head);
        ListNode head2 = reverseLinkedList(mid);

        while(head2 != null) {
            if(head.val != head2.val) {
                return false;
            }
            head = head.next;
            head2 = head2.next;
        }
        return true;
    }
}