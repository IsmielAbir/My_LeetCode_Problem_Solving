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
    public boolean isPalindrome(ListNode head) {
        Stack<Integer> s = new Stack<>();
        ArrayList<Integer> q = new ArrayList<>();
        while (head != null) {
            s.push(head.val);
            q.add(head.val);
            head = head.next;
        }
        while (!s.empty() && !q.isEmpty()) {
            if (s.peek() != q.get(0))
                return false;
            s.pop();
            q.remove(0);
        }
        return true;
    }
}
