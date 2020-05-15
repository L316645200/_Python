# 给定一个带有头结点head的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。
# 示例1：输入：[1, 2, 3, 4, 5]
# 输出：此列表中的结点3(序列化形式：[3, 4, 5])
# 返回的结点值为3 。 (测评系统对该结点序列化表述是[3, 4, 5])。
# 注意，我们返回了一个ListNode类型的对象ans，这样：ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及ans.next.next.next = NULL.
# 示例2：输入：[1, 2, 3, 4, 5, 6]
# 输出：此列表中的结点4(序列化形式：[4, 5, 6])
# 由于该列表有两个中间结点，值分别为3和4，我们返回第二个结点。
# 提示：
# 给定链表的结点数介于1和100之间。

# Definition for singly-linked list.

# TODO 第一次链表，不知链表为何物，一头雾水


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         A = [head]
#         while A[-1].next:
#             A.append(A[-1].next)
#         return A[len(A) // 2]

# 指针
# 遍历一次链表，记录下长度
# 第二次遍历到一半就可以得到中间节点

# 双指针
# 使用快慢两个指针，慢指针一次走一步，快指针一次走两步，当快指针走到头的时候，慢指针刚好走到一半
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
