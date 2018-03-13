#递归方法
def merge_sort(a,b,c):
    if len(a) == 0 or len(b) == 0:
        c.extend(a)
        c.extend(b)
    else:
        if a[0]<b[0]:
            c.append(a[0])
            del a[0]
        else:
            c.append(b[0])
            del b[0]
    return merge_sort(a,b,c)

#循环方法
def merge_sort(a,b):
    temp = []
    while len(a)>0 and len(b)>0:
        if a[0]<b[0]:
            tmp.append(a[0])
            del a[0]
        else:
            tmp.append(b[0])
            del b[0]
    tmp.extend(a)
    tmp.extend(b)
    return tmp

#pop方法

def merge_sort(a,b):
    tmp = []
    while a and b:
        if a[0]<b[0]:
            tmp.append(a.pop(0))
        else:
            tmp.append(b.pop(0))
     '''
     tmp.extend(a)
     tmp.extnd(b)
     '''
     while a:
        tmp.append(a.pop(0))
     while b:
        tmp.append(b.pop(0))
     return tmp
