#!/bin/python3

from typing import List

class Solution:


    def findMedianSortedArraysGpt(self, nums1, nums2):
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


    # Получение инициализирующих граничных индексов массивов
    def getInitEdgeIdx(self, nums):
        if len(nums)==0:
            return [-1, -1]
        
        return [0, len(nums)-1]

    # Проверка и получение граничных индексов 
    def getFixingEdgeIdx(self, nums, leftIdx, rightIdx):
        if len(nums)==0:
            return [-1, -1]

        # Если слева и справа массива значения равны, граничные индексы 
        # выставляются на самый левый элемент 
        # (оба указывают на самый левый элемент)
        if nums[leftIdx]==nums[rightIdx]:
            return [leftIdx, leftIdx]

        # Здесь гарантированно на концах массива разные значения

        if len(nums)>=3:

            # Если слева массива два повторяющихся значения
            # то нужно найти где повторяющееся значение заканчивается
            if nums[0]==nums[1]:

                # Бисекциями находится ячейка, где заканчивается
                # левое повторение значений
                # Результирующий индекс будет лежать в bisLeftIdx
                bisLeftIdx=0
                bisRightIdx=len(nums)-1
                while bisLeftIdx!=bisRightIdx:
                    bisMiddleIdx=((bisRightIdx-bisLeftIdx)//2)+bisLeftIdx
                    if bisLeftIdx==bisMiddleIdx:
                        break
                    if nums[0]==nums[bisMiddleIdx]:
                        bisLeftIdx=bisMiddleIdx
                    else:
                        bisRightIdx=bisMiddleIdx   
                leftIdx=bisLeftIdx

            # Если справа массива два повторяющихся значения
            # то нужно найти где повторяющееся значение заканчивается
            if nums[len(nums)-1]==nums[len(nums)-2]:

                # Бисекциями находится ячейка, где заканчивается
                # правое повторение значений
                # Результирующий индекс будет лежать в bisRightIdx
                bisLeftIdx=0
                bisRightIdx=len(nums)-1
                while bisLeftIdx!=bisRightIdx:
                    bisMiddleIdx=((bisRightIdx-bisLeftIdx)//2)+bisLeftIdx
                    if bisLeftIdx==bisMiddleIdx:
                        break
                    if nums[len(nums)-1]==nums[bisMiddleIdx]:
                        bisRightIdx=bisMiddleIdx
                    else:
                        bisLeftIdx=bisMiddleIdx   
                rightIdx=bisRightIdx

        return [leftIdx, rightIdx]
   

    def findMedianSortedArrays(self, 
                               nums1: List[int], 
                               nums2: List[int]) -> float:
        if len(nums1)==0 and len(nums2)==0:
            return None

        aLeftIdx, aRightIdx=self.getInitEdgeIdx(nums1)
        bLeftIdx, bRightIdx=self.getInitEdgeIdx(nums2)

        while True:
            # Подправляются индексы, если в заданном диапазоне
            # на концах есть повторяющиеся значения
            aLeftIdx, aRightIdx=self.getFixingEdgeIdx(nums1, aLeftIdx, aRightIdx)
            bLeftIdx, bRightIdx=self.getFixingEdgeIdx(nums2, bLeftIdx, bRightIdx)

            # Создается множество из крайних элементов
            # Иножество гарантирует что не будет повторов
            edgeValues=set()
            if aLeftIdx!=-1:
                edgeValues.add(nums1[aLeftIdx])
            if aRightIdx!=-1:
                edgeValues.add(nums1[aRightIdx])
            if bLeftIdx!=-1:
                edgeValues.add(nums2[bLeftIdx])
            if bRightIdx!=-1:
                edgeValues.add(nums2[bRightIdx])

            # Из множества получается отсортированный список крайних элементов 
            edgeValues=list(edgeValues).sort

            searchRange=[-1, -1]

            if len(edgeValues)==4:
                searchRange=[edgeValues[1], edgeValues[2]]
            elif len(edgeValues)==3:
                searchRange=[edgeValues[1], edgeValues[1]]
            elif len(edgeValues)==2:
                searchRange=[edgeValues[0], edgeValues[1]]
            elif len(edgeValues)==1:
                return float(edgeValues[1]) 
            elif len(edgeValues)==0:
                return None
                
            # Здесь считается что имеются все граничные значения

        return 1.0


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
