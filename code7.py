# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……
# 它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。


class Solution:
    def jumpFloorII(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        a = [0 for i in range(number)]
        print("len : " + str(len(a)))
        a[0] = 1
        a[1] = 2
        n = 3
        while n <= number:
            step_count = 0
            for i in range(n - 1, 0, -1):
                step_count = step_count + a[i - 1]
            new_step = step_count + 1
            a[n - 1] = new_step
            n += 1

        return a[-1]


if __name__ == "__main__":

    xx = Solution()
    for i in range(1, 10):
        print(xx.jumpFloorII(i))
