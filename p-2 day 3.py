"""def performBubbleSort(nums):
          n=len(nums)
          fixThisIndex=n-1
          
          while fixThisIndex > 0:
                  for index in range(fixThisIndex):
                          if nums[index]>nums[index +1]:
                                  temp=nums[index]
                                  nums[index]=nums[index + 1]
                                  nums[index + 1]=temp
                  print(nums)
                  fixThisIndex -= 1

nums=[10,8,2,14,12,7]
print("before sorting:",nums)
performBubbleSort(nums)
print("after sorting",nums)                               

def performSelectioneSort(nums):
          n=len(nums)
          fixThisIndex=n-1
          
          while fixThisIndex > 0:
                  maxEleIndex=fixThisIndex
                  for index in range(fixThisIndex):
                          if nums[index]>nums[maxEleIndex]:
                                  maxEleIndex = index
                          if maxEleIndex != fixThisIndex:
                                  temp=nums[maxEleIndex]
                                  nums[maxEleIndex]=nums[fixThisIndex]
                                  nums[fixThisIndex]=temp
                          print(nums)
                          fixThisIndex-=1
nums=[8,12,10,5,13,18]
print("before sorting:",nums)
performSelectioneSort(nums)
print("after sorting",nums)                             


def performInsertionSort(nums):
          n=len(nums)
          lastEleInSortArr = 0
          for firstIndex in range(1,n):
                  temp=nums[firstIndex]
                  previous=lastEleInSortArr
                   
          while previous >=0 and nums[previous]>temp:
                    nums[previous + 1]= nums[previous]
                    previous -= 1
          nums[previous + 1]=temp
          lastEleInSortArr += 1

nums=[10,8,2,14,12,7]
print("before sorting:",nums)
performInsertionSort(nums)
print("after sorting",nums)                    """


def mergeTwoSubarrays(nums, left, mid, right):
    temp = []
    index1 = left 
    index2 = mid + 1 
    while index1 <= mid and index2 <= right:
        if nums[index1] < nums[index2]:
            temp.append(nums[index1])
            index1 += 1
        else:
            temp.append(nums[index2])
            index2 += 1
 
    while index1 <= mid:
        temp.append(nums[index1])
        index1 += 1 
 
    while index2 <= mid:
        temp.append(nums[index2])
        index2 += 1    
 
    position = left 
    for ele in temp:
        nums[position] = ele 
        position += 1 
 
 
 
def mergeAndDivide(nums, left, right):
    if left >= right:
        return 
 
    mid = (left + right) // 2 
    mergeAndDivide(nums, left, mid)
    mergeAndDivide(nums, mid + 1, right)
    mergeTwoSubarrays(nums, left, mid, right)
 
 
 
def performMergeSort(nums):
    n = len(nums) 
    mergeAndDivide(nums, 0, n - 1)
 
nums = [10, 8, 2, 14, 12, 7, 9, 8, 4]
#nums = list(map(int, input().split()))
print("Before sorting:", nums)
 
performMergeSort(nums)
 
print("After sorting:", nums)