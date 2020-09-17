# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
'''
首先判断是否是二叉查找树：
    1. 左子树是二叉查找树
    2. 右子树是二叉查找树
    3. 根节点大于左子树最大值
    4. 根节点小于右子树最小值
注意在取当前二叉查找树最大子树和的时候要注意，最大的可能是子树的和而不是当前查找二叉树的和，所以不能直接
加
'''
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        
        def judge(node):
            if not node:
                return 1e9, -1e9, 0, True
            lmin, lmax, ls, is_lbst = judge(node.left)
            rmin, rmax, rs, is_rbst = judge(node.right)
            is_bst = False
            if lmax<node.val and rmin>node.val and is_lbst and is_rbst:
                is_bst = True
            min_val = min(node.val,lmin, rmin)
            max_val = max(node.val, lmax, rmax)
            if is_bst:
                s = ls+rs+node.val
            else:
                s = -1
            self.ans = max(s, self.ans)
            return min_val, max_val, s, is_bst
        self.ans = 0
        min_val, max_val, s, is_bst = self.judge(root)
        return self.ans
        
