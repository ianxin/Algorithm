#设步长为-1
def string_reverse(str):
    return str[::-1]

#for 循环，从右向左输出
def string_reverse(str):
    return ' '.join(str[i] for i in range(len(str)-1,0,-1))

#借用列表，使用Python内建的reverse()函数
def string_reverse(str):
    l = list(str)
    return ''.join(l.reverse())

#递归方法
def string_reverse(str):
    if str == '':
        reteun str
    else:
        return string_reverse(str[1:])+str[0]
