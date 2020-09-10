# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            traverse(self, root, 0)
        return root
    def traverse(self, node:TreeNode, diff):
        if node.right:
            rdiff = traverse(node.right, diff)
            node.val += rdiff
        else:
            node.val += diff
        
        if node.left:
            ldiff = traverse(node.left, node.val)
            return ldiff
        else:
            return node.val
        