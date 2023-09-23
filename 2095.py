# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        fast = head
        slow = head
        root = head

        while fast and fast.next:
            slow = head
            head = head.next
            fast = fast.next.next

        slow.next = head.next

        return root