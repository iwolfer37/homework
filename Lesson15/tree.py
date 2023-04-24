class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        elif data < self.data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.insert(data)

    def insert_list(self, data_list):
        for data in data_list:
            self.insert(data)

    def min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.data

    def max_value(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.data

    def remove(self, value):
        if self is None:
            return self

        if value < self.data:
            if self.left is not None:
                self.left = self.left.remove(value)
        elif value > self.data:
            if self.right is not None:
                self.right = self.right.remove(value)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_right = self.right
                while min_right.left is not None:
                    min_right = min_right.left
                self.data = min_right.data
                self.right = self.right.remove(min_right.data)

        return self

tree = Tree()
data_list = [5, 3, 8, 4, 37, 11, 7, 6, 2]
tree.insert_list(data_list)

#ми видаляємо двійку, тоді мінімальне значення буде 3:
tree.remove(2)
print(tree.min_value())
print(tree.max_value())
