class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        dum = head
        while dum.next:
            dum = dum.next
            length += 1
        tail = dum
        tail.next = head

        k = k % length
        if k == 0:
            tail.next = None
            return head

        steps = length - k - 1
        dum = head
        for _ in range(steps):
            dum = dum.next

        new_head = dum.next
        dum.next = None

        return new_head
