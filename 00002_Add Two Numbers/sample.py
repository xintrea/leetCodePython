#!/bin/python

# Решил прямо в браузере, здесь нет вызова с проверочными данными

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, 
                      l1: Optional[ListNode], 
                      l2: Optional[ListNode]) -> Optional[ListNode]:

        a=0
        mul=1
        while l1 is not None:
            a += l1.val * mul
            mul *= 10
            l1 = l1.next

        b=0
        mul=1
        while l2 is not None:
            b += l2.val * mul
            mul*=10
            l2 = l2.next

        summ=a+b
        firstNode=None
        prevNode=None

        while summ!=0:
            currNode = ListNode()
            if firstNode is None:
                firstNode = currNode

            divRemain=summ % 10
            
            # result.append(divRemain)
            currNode.val = divRemain
            if prevNode is not None:
                prevNode.next = currNode

            summ=(summ-divRemain) // 10

            prevNode=currNode

        if firstNode is None:
            return ListNode(0)
        else:    
            return firstNode

