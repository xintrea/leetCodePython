#!/bin/python3

from typing import List

class Solution:
    def findMedianSortedArrays(self, 
                               nums1: List[int], 
                               nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]

            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]

            if maxX <= minY and maxY <= minX:
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1


solutin=Solution()

'''
nums=[]
nums.append([5,5,5,5,9])
nums.append([5,5,5,5,5,9])
nums.append([5,5,9,9,9])
nums.append([5,5,9,9,9,9])
nums.append([5,5,9,9,9,9])
nums.append([1,2,3,5,5,5])
nums.append([1,2,3,5,5])
nums.append([5,5,5,5,5])

for n in nums:
    print("Проверяется массив: "+str(n))

    aLeftIdx, aRightIdx=solutin.getInitEdgeIdx(n)
    print("Инициализирующие индексы: "+str(aLeftIdx)+" "+str(aRightIdx))

    aLeftIdx, aRightIdx=solutin.getFixingEdgeIdx(n, aLeftIdx, aRightIdx)
    print("Исправленные индексы: "+str(aLeftIdx)+" "+str(aRightIdx))

exit(0)
'''

# a=[1, 3, 5, 7]
# b=[2, 6, 10]

a=[1, 8, 9, 10]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a)
print(b)
i=solutin.findMedianSortedArraysGpt(a, b)

print(i)
