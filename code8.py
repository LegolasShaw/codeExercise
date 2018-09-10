# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        count = 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        n = 3
        pre_count = 2
        prepre_count  = 1
        while n <= number :
            count = pre_count + prepre_count
            prepre_count = pre_count
            pre_count = count
            n += 1

        return count
xx = Solution()
for i in range(1, 10):
    print(xx.rectCover(i))
