# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans=ListNode(0)
        tail=ans
        next_add=0
        while l1 or l2 or next_add!=0:
            l1 = l1 if l1 else ListNode(0)
            l2 = l2 if l2 else ListNode(0)
            val=l1.val+l2.val+next_add
            next_add=val//10
            tail.next=ListNode(val%10)
            tail=tail.next
            l1=l1.next
            l2=l2.next
        ans=ans.next
        return ans
L1=ListNode(9,ListNode(9,ListNode(9,ListNode(9))))
L2=ListNode(9,ListNode(9))
ans=Solution().addTwoNumbers(L1,L2)

while ans:
    print(ans.val)
    ans=ans.next
