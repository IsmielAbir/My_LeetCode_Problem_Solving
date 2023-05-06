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

    int countLength(ListNode head){
        int c=0;
        ListNode temp=head;
        while(temp!=null){
            temp=temp.next;
            c++;
        }
        return c;
    }

    public ListNode middleNode(ListNode head) {
        int size = countLength(head);
        int s= size/2;
        for(int i=1;i<=s;i++){
            head=head.next;
        }
        return head;
    }
}