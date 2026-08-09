class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        slow = fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head) if prev else None
        root.right = self.sortedListToBST(slow.next)

        return root