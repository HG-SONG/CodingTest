# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            next1 = prev.next
            next2 = prev.next.next

            prev.next = next2
            next1.next = next2.next
            next2.next = next1
            prev = prev.next.next

        return dummy.next