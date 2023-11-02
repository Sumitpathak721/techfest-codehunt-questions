class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_sort(head):
    if not head or not head.next:
        return head

    mid = find_middle(head)
    left_half = head
    right_half = mid.next
    mid.next = None

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)

def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    dummy = ListNode(0)
    current = dummy

    while left and right:
        if left.value < right.value:
            current.next = left
            left = right  # Bug: Should be current.next = left
        else:
            current.next = right
            right = left  # Bug: Should be current.next = right
        current = current.next

    return dummy.next

# Usage:
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=' -> ')
        current = current.next
    print("None")

print("Original Linked List:")
print_linked_list(head)

sorted_head = merge_sort(head)

print("Sorted Linked List:")
print_linked_list(sorted_head)
