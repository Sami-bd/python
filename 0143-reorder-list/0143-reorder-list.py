# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr_node = head
        fast_node = head
        slow_node = head
        while fast_node and fast_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

        def reverse_list(node):
            prev_node = None
            while node:
                next_node = node.next
                node.next = prev_node
                prev_node = node
                node = next_node

            return prev_node

        second_half = reverse_list(slow_node)
        while curr_node and second_half.next:
            tmp1 = curr_node.next
            tmp2 = second_half.next
            curr_node.next = second_half
            second_half.next = tmp1
            curr_node = tmp1
            second_half = tmp2