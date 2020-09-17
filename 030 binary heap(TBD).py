class Node：
    def __init__(self, p, l, r, v):
        self.parent = p
        self.left_child = l 
        self.right_child = r 
        self.value = v
    def get_left_child(self):
        return self.left_child 
    def get_right_child(self):
        return self.right_child 
    def get_parent(self):
        return self.parent

class Tree:
    def __init__(self):
        self.root = Node(None, None, None, None)
    def add(self, value:int):
        if self.root.value:
            index = self.root
            while index:
                if index.value>value:
                    index = index.get_left_child()
                else:
                    idnex = index.git_right_child()
            new_node = Node(index, None, None, value)
            index.
        else:
            self.root.value = value

    def find(self, value:int):
        index = self.root
        result = False
        while index.value != value and index:
            if value<index.value:
                index = index.get_left_child()
            else:
                index = index.get_right_child()
            if index.value == value:
                result = True
            break
        if result:
            return index
        else:
            return result
    def delete(self, value):
        index = self.find(value)
        if not index:
            return 
        else:
            if not index.get_left_child():
                index.get_parent().right_child = index.left_child
                return 
            if not index.get_right_child():
                index.get_parent().right_child = index.right_child
            