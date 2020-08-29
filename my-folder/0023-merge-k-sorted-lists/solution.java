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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        return merge(lists, 0, lists.length - 1);
    }
    
    private ListNode merge(ListNode[] lists, int low, int high) {
        if (low == high) return lists[low];
        if (low + 1 == high) return mergeTwoSortedLists(lists[low], lists[high]);
        
        int mid = low + (high - low) / 2;
        ListNode l1 = merge(lists, low, mid);
        ListNode l2 = merge(lists, mid + 1, high);
        return mergeTwoSortedLists(l1, l2);
    }
    
    private ListNode mergeTwoSortedLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        
        ListNode dummy = new ListNode(-1);
        ListNode curr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        
        if (l1 != null) curr.next = l1;
        if (l2 != null) curr.next = l2;
        
        return dummy.next;
    }
}
