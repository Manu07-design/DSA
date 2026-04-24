# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        PA = headA
        PB = headB
        while PA != PB:
            PA = PA.next if PA else headB
            PB = PB.next if PB else headA
        return PA