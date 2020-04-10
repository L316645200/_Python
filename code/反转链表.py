class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
            print(rev, rev.next, p)
        return rev


s = Solution()
s.reverseList([5, 4, 3, 2, 1])



