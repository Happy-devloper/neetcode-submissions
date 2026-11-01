# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second_half = slow.next
        slow.next = None
        prev = None
        curr = second_half
        while curr:
            nxt = curr.next
            curr.next= prev
            prev = curr
            curr = nxt
        second_half = prev
        first_half = head
        while second_half:
            temp1 = first_half.next
            temp2 = second_half.next
            first_half.next = second_half
            second_half.next = temp1

            first_half = temp1
            second_half = temp2        