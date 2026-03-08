# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):

        # Base case
        if not head or not head.next:
            return head

        # Step 1: Find middle using slow-fast pointer
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list
        mid = slow.next
        slow.next = None

        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge sorted halves
        return self.merge(left, right)


    def merge(self, l1, l2):

        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:

            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        # Attach remaining nodes
        curr.next = l1 if l1 else l2

        return dummy.next


# -------- Helper Functions for Testing --------

def create_linked_list(arr):
    dummy = ListNode()
    curr = dummy

    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# -------- Test Example --------

arr = [4, 2, 1, 3]

head = create_linked_list(arr)

print("Original List:")
print_list(head)

solution = Solution()
sorted_head = solution.sortList(head)

print("Sorted List:")
print_list(sorted_head)