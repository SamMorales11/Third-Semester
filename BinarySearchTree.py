class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current_node, new_node):
        if new_node.value < current_node.value: # ke kiri jika nilai lebih kecil dari root
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursive(current_node.left, new_node)
        elif new_node.value > current_node.value: #ke sebelah kanan jika node lebih besar dari rooy
        
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursive(current_node.right, new_node)

    def search(self, value): #mencari nilai tertentu dalam BST
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value): #memanggil method _search_recursive
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    def inorder_traversal(self): #membuat daftar kosong untuk menyimpan hasil
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, current_node, result): # memulai rekursif dari node kiri dan berakhir di node kanan
        if current_node:
            self._inorder_traversal_recursive(current_node.left, result)
            result.append(current_node.value)
            self._inorder_traversal_recursive(current_node.right, result)

# Example usage:
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(15)
bst.insert(25)
bst.insert(36)

print(bst.search(4)) 
print(bst.search(6))  
print(bst.search(100))

print(bst.inorder_traversal())  