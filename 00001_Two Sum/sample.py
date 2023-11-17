#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
  
    def addTwoNumbers(self, l1, l2) :

        a=0
        mul=1
        while l1 is not None:
            a += l1.val * mul
            mul *= 10
            l1 = l1.next

        print("a:"+str(a))

        b=0
        mul=1
        while l2 is not None:
            b += l2.val * mul
            mul*=10
            l2 = l2.next

        print("b:"+str(b))

        summ=a+b
        
        print("summ:"+str(summ))
        
        result=[]

        while summ!=0:
            divRemain=summ % 10
            print("divRemain:"+str(divRemain))
            
            result.append(divRemain)
            print("result:"+str(result))
            
            summ=(summ-divRemain) // 10
            print("summ:"+str(summ))

        return result

s=Solution()


a1=ListNode()
a1.val=2

a2=ListNode()
a2.val=4

a3=ListNode()
a3.val=3

a1.next=a2
a2.next=a3


b1=ListNode()
b1.val=5

b2=ListNode()
b2.val=6

b3=ListNode()
b3.val=4

b1.next=b2
b2.next=b3

s.addTwoNumbers( a1, b1 )
