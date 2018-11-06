class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start:
                if start.value == find_val:
                    return True
                else:
                    val = self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
                    return val

        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.insert_help(self.root, new_val)

    def search(self, find_val):
        return self.search_help(self.root, find_val)

    def insert_help(self, start, new_val):
        if start.value < new_val:
            if start.right:
                self.insert_help(start.right, new_val)
            else:
                start.right = Node(new_val)
        else:
            if start.left:
                self.insert_help(start.left, new_val)
            else:
                start.left = Node(new_val)

    def search_help(self, start, find_val):
        if start.value == find_val:
            return True
        elif start.value < find_val:
            self.search_help(start.right, find_val)
        else:
            self.search_help(start.left, find_val)
        return False


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
