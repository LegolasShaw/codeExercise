

'''
题目描述
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
'''

class Solution:
    def Find(self, target, array):
        n_row = len(array)
        m_col = len(array[0])
        if (n_row == 0) or (m_col == 0):
            return False
        for row in array:
            if (row[0] <= target) and (target <= row[m_col - 1]):
                for temp in row:
                    if temp == target:
                        return True
            if row[0] > target:
                return False
        return False


class Solution1:
    def Find(self, target, array):
        n_row = len(array)
        m_col = len(array[0])
        i = n_row -1
        j = 0
        while i >= 0 and j <= m_col -1:
            if array[i][j] <target:
                j += 1
            elif array[i][j] > target:
                i -= 1
            else:
                return True

        return False


'''
另外一种思路是：
利用二维数组由上到下，由左到右递增的规律，
那么选取右上角或者左下角的元素a[row][col]与target进行比较，
当target小于元素a[row][col]时，那么target必定在元素a所在行的左边,
即col--；
当target大于元素a[row][col]时，那么target必定在元素a所在列的下边,
即row++；
'''







