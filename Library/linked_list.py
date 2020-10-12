# Common Library 
from typing import List, Dict

class ListNode: 
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, nums: List[int]) -> None:
        self.head = self.initList(nums)
    
    def initList(self, nums: List[int]) -> ListNode:
        head, dummy = None, None
        for num in nums:
            if not dummy:
                dummy = ListNode(num)
                head = dummy
            else:
                dummy.next = ListNode(num)
                dummy = dummy.next
        return head
                
    def head(self) -> ListNode:
        return self.head
