#-*- coding: utf-8 -*-

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。


class Solution:
    def jumpFloor(self, number):
        n = 3
        prepre_count = 1
        pre_count = 2
        cur_count = 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        while n <= number:
            cur_count = pre_count + prepre_count
            prepre_count = pre_count
            pre_count = cur_count
            n += 1
        return cur_count