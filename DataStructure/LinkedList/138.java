/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        //creat interweaving
        Node cur = head;
        while(cur != null) {
            cur.next = new Node(cur.val, cur.next);
            cur = cur.next.next;
        }

        //copy random pointer
        cur = head;
        while(cur != null) {
            if(cur.random != null) {
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next;
        }

        //return the list and recover the original list.
        Node dummy = new Node(5);
        Node copyCur = dummy;

        cur = head;
        while(cur != null) {
            Node copy = cur.next;
            copyCur.next = copy;
            copyCur = copyCur.next;
            
            //recover the original list.
            cur.next = cur.next.next;
            cur = cur.next;
        }
        return dummy.next;
    }
}