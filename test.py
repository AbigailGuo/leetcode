class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def get_sorted_array( node, array): 
        if node.left:
            get_sorted_array(node.left, array)
        array.append(node)
        if node.right:
            get_sorted_array(node.right, array)
        return array

root = TreeNode(4, None, None)
one = TreeNode(1, None, None)
five = TreeNode(5, None, None)
root.left = one
root.right = five
new_array = []
new_array = get_sorted_array(root, new_array)
for i in new_array:
    print(i.val)