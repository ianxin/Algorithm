#使用set去除元素，改变了数组顺序
def removeDuplicates(nums):
    # write your code here
    nums = list(set(nums))
    return nums

#用字典
def removeDuplicates(nums):
    # write your code here
    nums = {}.fromkeys(nums).keys()
    return nums
#用字典并保持顺序
def removeDuplicates(nums):
    # write your code here
    l = list(set(nums))
    l.sort(key=nums.index)
    return l

#使用遍历，不改变顺序
def removeDuplicates(nums):
    l1=[]
    return [l1.append(i) for i in nums if not i in l1]

'''
给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。

不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。
'''
def removeDuplicates(self, nums):
        # write your code here
        if len(nums) ==0:
            return 0
        k=0
        for i in range(1,len(nums)):
            if nums[i] != nums[k]:
                k+=1
                nums[k] = nums[i]
        
        del nums[k+1:len(nums)]
        return len(nums)
