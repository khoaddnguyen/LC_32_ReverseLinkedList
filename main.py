class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Two Pointers: Time O(n), Memory O(1)

        # prev, curr = None, head
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev


        # Recursive: Time O(n), Memory O(n)
        if not head:  # if head is null, return null
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead