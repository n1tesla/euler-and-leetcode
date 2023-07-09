from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merged_list=[]


        if list1:
            for i in list1:
                merged_list.append(i)
        if list2:
            for j in list2:
                merged_list.append(j)

        sorted_list=sorted(merged_list)
        return sorted_list

list1 = []
list2 = [0]

sol=Solution()
print(sol.mergeTwoLists(list1,list2))
