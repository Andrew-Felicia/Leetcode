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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode result = new ListNode(5);
        ListNode tmp = result;

        while(list1 != null && list2 != null) {
            if(list1.val <= list2.val) {
                tmp.next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                tmp.next = new ListNode(list2.val);
                list2 = list2.next;
            }
            tmp = tmp.next;
        }
        tmp.next = (list1 == null) ? list2 : list1;
        return result.next;
    }
}