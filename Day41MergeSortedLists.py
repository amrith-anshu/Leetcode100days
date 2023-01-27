class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = curNode = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curNode.next = list1
                list1 = list1.next
            else:
                curNode.next = list2
                list2 = list2.next
            curNode = curNode.next
        
        curNode.next = list1 if list1 else list2
        

        return head.next
