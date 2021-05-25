import random

from ds_coding_interviews_in_python.ch6trees.bst import BinarySearchTree, display

BST = BinarySearchTree(50)
for _ in range(15):
    ele = random.randint(0, 100)
    print("Inserting " + str(ele) + ":")
    BST.iter_insert(ele)
    # We have hidden the code for this function but it is available for use!
    display(BST.root)
    print("\n")
print(BST.iter_search(50))  # Will print True since 50 is the root
print(BST.iter_search(111))  # May or may not be True. Check the tree!

BST = BinarySearchTree(50)
for _ in range(15):
    ele = random.randint(0, 100)
    print("Inserting " + str(ele) + ":")
    BST.recursive_insert(ele)
    # We have hidden the code for this function but it is available for use!
    display(BST.root)
    print("\n")
print(BST.recursive_search(50))  # Will print True since 50 is the root
print(BST.recursive_search(111))  # May or may not be True. Check the tree!

BST = BinarySearchTree(6)
BST.iter_insert(3)
BST.iter_insert(2)
BST.iter_insert(4)
BST.iter_insert(-1)
BST.iter_insert(1)
BST.iter_insert(-2)
BST.iter_insert(8)
BST.iter_insert(7)

print("before deletion:")
display(BST.root)

BST.delete(-2)
print("after deletion:")
display(BST.root)
