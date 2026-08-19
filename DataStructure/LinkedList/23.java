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

import java.util.Arrays;

class Solution {
    //this function merge two sorted list to one sorted list.
    private ListNode mergeTwoLists(ListNode l, ListNode r) {
        ListNode dummy = new ListNode(5);
        ListNode tmp = dummy;
        while(l != null && r != null) {
            if(l.val <= r.val) {
                tmp.next = new ListNode(l.val);
                tmp = tmp.next;
                l = l.next;
            } else {
                tmp.next = new ListNode(r.val);
                tmp = tmp.next;
                r = r.next;
            }
        }
        tmp.next = (l == null)? r : l;
        return dummy.next;
    }

    //merge k sorted lists to one sorted list and return it.
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0 || lists == null) return null;
        if(lists.length == 1) return lists[0];
        if(lists.length == 2) return mergeTwoLists(lists[0], lists[1]);

        int listSize = lists.length;
        int mid = listSize / 2;
        ListNode left = mergeKLists(Arrays.copyOfRange(lists, 0, mid));
        ListNode right = mergeKLists(Arrays.copyOfRange(lists, mid, lists.length));
        return mergeTwoLists(left, right);
    }
}