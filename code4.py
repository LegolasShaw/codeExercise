# -*- coding:utf-8 -*-
#题目描述
#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

class Solution:
    stack1 = []
    stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                node = self.stack1.pop(-1)
                self.stack2.append(node)
        if len(self.stack2) > 0:
            node = self.stack2.pop()
            return node

