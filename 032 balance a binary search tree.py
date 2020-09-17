# https://leetcode.com/problems/balance-a-binary-search-tree/
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balance_bst(self, root: TreeNode):
         array = []
        if root:
            array = self.get_sorted_array(root, array)
        print(len(array))
        return self.build_tree(array, 0, len(array)-1)

    # 首先利用二叉平衡树的性质写出排序后的数组
    def get_sorted_array(self, node, array): 
        if node.left:
            self.get_sorted_array(node.left, array)
        array.append(node)
        if node.right:
            self.get_sorted_array(node.right, array)
        return array
    def build_tree(self, array, left, right):
        # mid = int((left+right)/2
        # if int((left+mid)/2)>0:
        #     node.left = array[int((left+mid)/2)]
        #     self.build_tree(node.left, left, mid)
        # if int((mid+right)/2)<right:
        #     node.right = array[int((mid+right)/2)]
        #     self.build_tree(node.right, mid, right)
        if left>right:
            return None
        mid = int((left+right)/2)
        root = array[mid]
        root.left = self.build_tree(array, left, mid-1)
        root.right = self.build_tree(array, mid+1, right)
        return root
