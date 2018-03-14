# 冒泡排序(O(n^2))
def bubblesort(relist):
    length = len(relist)
    for i in range(length):
        for j in range(length-i-1):
            if relist[j]>relist[j+1]:
                relist[j+1],relist[j] = relist[j],relist[j+1]
            else: pass
    return relist


#选择排序法

def selectsort(relist):
    length = len(relist)
    for i in range(length):
        min_index = i
        for j in range(i+1,length):
            if relist[j]<relist[min_index]:
                min_index = j
        relist[i],relist[min_index] = relist[min_index],relist[i]
    return relist




#快速排序法， O(nlogn)

def quicksort(relist):
    if len(relist)<2:
        return relist
    else:
        base_point = relist[0]
        less = [i for i in relist[1:] if i<base_point]
        greater = [i for i in relist[1:] if i>base_point]
        return quicksort(less)+[base_point]+quicksort(greater)

print(quicksort([2,3,1,4,6,5,7,9,8]))

#插入排序
def insertsort(relist):
    length = len(relist)
    for i in range(1,length):
        for j in range(i):
            if relist[i]<relist[j]:
                relist.insert(j,relist[i])
                relist.pop(i+1)
                break
    return relist



#二分法，数组必须是有序的 O(logn)
def binary_search(relist,item):
    low = 0
    high = len(relist)-1
    #第一个元素就满足的情况
    if relist[low] == item:
        return low
    while low<=high:
        #mid = (low+high)>>1
        mid = (low+high)//2 #python3 向下取整
        guess = relist[mid]
        if guess<item:
            low = mid+1
        elif guess>item:
            high = mid-1
        else: 
            return mid
    return None



