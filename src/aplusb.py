class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    异或=不考虑进位的加法
    与=只考虑进位
    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        if b == 0:
            return a
        if a == 0:
            return b
        while b:
            carry = (a&b)<<1 
            a = a ^ b
            b = carry
        return a
    def aplusb(self,a, b):
    # write your code here, try to do it without arithmetic operators.
    limit = 0xfffffffff
    while b:
        a, b = (a ^ b) & limit, (a & b) << 1
    return a if a & 1 << 32 == 0 else a | (~limit)
