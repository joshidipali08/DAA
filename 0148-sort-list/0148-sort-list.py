class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        arr.sort()

        head = ListNode(arr[0])
        cur = head

        for x in arr[1:]:
            cur.next = ListNode(x)
            cur = cur.next

        return head