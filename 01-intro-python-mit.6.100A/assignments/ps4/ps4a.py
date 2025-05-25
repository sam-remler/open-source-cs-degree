from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

def find_tree_height(tree : Node):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    if tree is None:
        return -1
    else:
        left_tree_height = 1 +  find_tree_height(tree.get_left_child())
        right_tree_height = 1 + find_tree_height(tree.get_right_child())

        return max ( left_tree_height, right_tree_height)

def is_heap(tree : Node, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    if tree is None:
        return True
    
    left = tree.get_left_child()
    right = tree.get_right_child()
    valid = True
    
    if left:
        valid = valid and compare_func(left.get_value(), tree.get_value())
        valid = valid and is_heap(left, compare_func)
    
    if right:
        valid = valid and compare_func(right.get_value(), tree.get_value())
        valid = valid and is_heap(right, compare_func)

    return valid

if __name__ == '__main__':

    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
