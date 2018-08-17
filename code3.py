'''输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回
'''

# -*- coding:utf-8 -*-

from queue import Queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
	def reConstructBinaryTree(self, pre, tin):
		if len(pre) == 0 or len(tin) == 0 :
			return None
		root_node = TreeNode(pre.pop(0))
		index = -1
		for i in range(len(tin)):
			if TreeNode(tin[i]).val == root_node.val:
				index = i
				break
		new_left = tin[:index]
		new_right = tin[index +1:]
		root_node.left = self.reConstructBinaryTree(pre, new_left)
		root_node.right = self.reConstructBinaryTree(pre, new_right)
		return root_node


'''
给定一个二叉树序列 返回前序遍历，中序遍历，后序遍历
'''

def test():
	sl =  Solution()
	root_node = sl.reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
	return root_node


def pre_view_tree(root_node, view_list):
	if root_node is not None:
		view_list.append(root_node.val)
		if root_node.left is not None:
			pre_view_tree(root_node.left, view_list)
		if root_node.right is not None:
			pre_view_tree(root_node.right, view_list)


def pre_view_tree_stack(root_node, view_list):
	stack = []
	while (root_node is not None) or (len(stack)> 0):
		while root_node is not None:
			stack.append(root_node)
			view_list.append(root_node.val)
			root_node = root_node.left
		if len(stack) > 0:
			root_node = stack.pop(-1).right
			

def mid_view_tree(root_node ,view_list):
	if root_node is not None:
		if root_node.left is None:
			mid_view_tree(root_node.left, view_list)
		view_list.append(root_node.val)
		if root_node.right is None:
			mid_view_tree(root_node.right, view_list)

def mid_view_tree_stack(root_node ,view_list):
	stack = []
	while (root_node is not None) or (len(stack) > 0) :
		while root_node is not None:
			stack.append(root_node)
			root_node = root_node.left
		if len(stack) >0:
			root_node = stack.pop(-1)
			view_list.append(root_node.val)
			root_node = root_node.right

def wsearch(root_node, view_list):
	q= Queue()
	while root_node is not None :
		view_list.append(root_node.val)
		if root_node.left is not None:
			q.put(root_node.left)
		if root_node.right is not None:
			q.put(root_node.right)
		if q.empty() == False:
			root_node = q.get()
		else:
			root_node = None


			
if __name__ == '__main__':
	tree_root = test()
	view_list = []
	wsearch(tree_root, view_list)
	print(view_list)


	

