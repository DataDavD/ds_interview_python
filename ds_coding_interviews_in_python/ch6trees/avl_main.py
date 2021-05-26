from ds_coding_interviews_in_python.ch6trees.avl import AVLTree

avl_tree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = avl_tree.insert_node(root, num)
avl_tree.print_helper(root, "", True)
key = 33
root = avl_tree.delete_node(root, key)
print("After Deletion: ")
avl_tree.print_helper(root, "", True)
