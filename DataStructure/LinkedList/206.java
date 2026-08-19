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

//TC: O(n)
//SC: O(n)
// //this algorithms will cost extra space, but easy to understand.
// import java.util.List;
// import java.util.ArrayList;
// import java.util.Collections;
// //iterative version.
// class Solution {
//     public ListNode reverseList(ListNode head) {
//         if(head == null || head.next == null) return head;

//         List<Integer> elements = new ArrayList<>();

//         ListNode tmp = head;
//         while(tmp != null) {
//             elements.add(tmp.val);
//             tmp = tmp.next;
//         }

//         Collections.reverse(elements);

//         ListNode result = new ListNode(5); //dummy node.
//         tmp = result; 
//         for(int i : elements) {
//             tmp.next = new ListNode(i);
//             tmp = tmp.next;
//         }

//         return result.next;
//     }
// }

//TC: O(n^2)
//SC: O(1)
//this algprithm is very similar to reverse the elements inside a list.
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;

        while(cur != null) {
            ListNode next = cur.next; //save the linked list.
            cur.next = prev;
            prev = cur;
            cur = next;
        }

        return prev;



    }

}