# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        # Push the head of each non-empty linked list into the heap
        for i in range(len(lists)):
            if lists[i]:
                heappush(minHeap, (lists[i].val, i, lists[i]))

        dummy= ListNode(0)
        pointer = dummy

        # Continue merging while there are nodes in the heap
        while minHeap:
            value, i, curr = heappop(minHeap)
            pointer.next = curr
            pointer = pointer.next

            # If the current node has a next, push it into the heap
            if curr.next:
                heappush(minHeap, (curr.next.val, i, curr.next))

        return dummy.next
        
        