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
    // d->1->1->1->2->3
    
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode prev = dummy;
        ListNode cur = head;
        while(cur!=null&&cur.next!=null){
            while(cur.next!=null&&cur.val==cur.next.val){
                cur = cur.next;
            }
            // cur could be 
            // 1. if duplicate, the last one
            // 2. a distinct one
            if(prev.next == cur){ // a distinct one
                prev = prev.next;
                cur = cur.next;
            }else{                // skip the last one
                prev.next = cur.next;
                cur = cur.next; 
            }
        }
        return dummy.next;
    }
}
