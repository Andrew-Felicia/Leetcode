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

//TC:O(nlog(n))
//SC:O(log(n))
class Solution {
    //find the middle node of the list.
    private ListNode findMiddle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        ListNode pre = null;
        
        while(fast != null && fast.next != null) {
            pre = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        pre.next = null;
        return slow;
    }
    
    //merge two sorted list to one sorted list.
    private ListNode merge(ListNode head1, ListNode head2) {
        ListNode dummy = new ListNode(5);
        ListNode tmp = dummy;

        while(head1 != null && head2 != null) {
            if(head1.val <= head2.val) {
                tmp.next = new ListNode(head1.val);
                head1 = head1.next;
                tmp = tmp.next;
            } else {
                tmp.next = new ListNode(head2.val);
                head2 = head2.next;
                tmp = tmp.next;
            }
        }

        tmp.next = (head1 == null) ? head2 : head1;
        return dummy.next;
    }

    //this recursive function return the sorted list.
    public ListNode sortList(ListNode head) {
        //base case.
        if(head == null || head.next == null) return head;

        ListNode head2 = findMiddle(head);

        head2 = sortList(head2);
        head = sortList(head);

        return merge(head, head2);
    } 
}