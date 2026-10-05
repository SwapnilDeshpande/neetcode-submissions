# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        newHead = newList
        while list1 and list2 :
            if list1.val <= list2.val :
                newList.next = list1
                list1 = list1.next
            else :
                newList.next = list2
                list2 = list2.next

            newList = newList.next
        # If list1 has more elements than list2 append remaining elements to new list
        if list1:
            while list1:
                newList.next = list1
                list1 = list1.next
                newList = newList.next
        # If list2 has more elements than list1 append remaining elements to new list
        if list2:
            while list2:
                newList.next = list2
                list2 = list2.next
                newList = newList.next
        return newHead.next