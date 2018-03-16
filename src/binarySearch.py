'''
经典二分法
适用于没有重复元素的有序数组
'''
def binarySearch(nums,target):
    if len(nums) == 0:
        return -1
    start = 0
    end = len(nums)-1
    while start+1 < end:
        mid = (start+end)>>1
        if nums[mid]>target:
            end = mid
        elif nums[mid]<target:
            start = mid
        else:
            return mid
     return -1

'''
给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1
在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2

'''
def binarySearch(nums,target):
    if len(nums) == 0:
        return -1
    start = 0
    end = len(nums)-1
    while start+1<end:
        mid = (start+end)>>1
        if nums[mid]>=target:
            end = mid
        else:
            start = mid
    if nums[start] == target:
        return start
    if nums[start] == target:
        return end
    return -1

'''
给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target最后一次出现的下标（从0开始），如果target不存在于数组中，返回-1
在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回3
'''
def binarySearch(nums,target):
    if len(nums)==0:
        return -1
    start = 0
    end = len(nums)-1
    while start+1<end:
        mid = (start+end)>>1
        if nums[mid]<=target:
            start = mid
        else:
            end = mid
    if nums[end] == target:
        return end
    if nums[start] == target:
        return start
    return -1

'''
在一个有序数组中，给定一个target，要求在数组中找到离target最近的数。

Given [1, 4, 6] and target = 3, return 1.

Given [1, 4, 6] and target = 5, return 1 or 2.

Given [1, 3, 3, 4] and target = 2, return 0 or 1 or 2.
'''
def closetNumber(nums, target):
    if len(nums) == 0:
        return -1
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = (start + end) >> 1
        if nums[mid] > target:
            end = mid
        elif nums[mid] < target:
            start = mid
        else:
            return mid
    left = abs(nums[start]-target)
    right = abs(nums[end]-target)

    return start if left<right else end

'''
求有序数组中某个target出现了多少次
'''
#简便方法
def totalOccurrence(nums,target):
    return nums.count(target)

#利用二分法，先找到target第一次出现的位置，然后再遍历列表

def totalOccurance(nums,target):
    if len(nums) == 0:
        return -1
    start = 0
    end = len(nums)-1
    while start+1<end:
        mid = (start+end)>>1
        if nums[mid]>=target:
            end = mid
        else:
            start = mid
     if nums[start] == target:
        count = 0
        for i in nums[start:len(nums)-1]
            if i == target:
                count+=1
        return count
     if nums[end] == target:
        count = 0
        for i in nums[end:len(nums)-1]:
            if i == target:
                count+=1
        return count
