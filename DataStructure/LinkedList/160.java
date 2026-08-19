/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode q = headA;
        ListNode p = headB;

        while(q != p) {
            p = (p != null) ? p.next : headA;
            q = (q != null) ? q.next : headB;
        }
        return p;
    }
}