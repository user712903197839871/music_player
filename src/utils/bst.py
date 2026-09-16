# i cant belive i need to build it from scratch, 
# isn't there a python library called ai you do import ai ai.learn() and that's it
# how come that there isnt a ds.bst


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value



class BST:
    def __init__(self, start_value=None, comparator=lambda a, b: a > b):
        """
        creates a BST

        Args:
            start_value - a starting value
            comparator - the custom comparator function
        """
        
        self.head = Node(value=start_value)
        self.comparator = comparator


    def insert(self, value):
        if self.head.value == None:
            self.head.value = value
            return
        
        temp: Node = self.head

        while temp is not None:
            if self.comparator(temp.value, value):
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = Node(value=value)
                    return
            else:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = Node(value=value)
                    return

    
    def in_order(self, func, limit: int=-1):
        """
        passes through tree in order and executes func on each step

        Args:
            func - function to execute at each step
            limit - how many steps to execute func
        """

        node: Node = self.head

        def traverse(node, limit):
            if not node or limit[0] == 0:
                return
            
            traverse(node.left, limit)
            if limit[0] == 0:
                return

            func(node)
            limit[0] -= 1
            traverse(node.right, limit)

        traverse(node, [limit])


    def print_node(self, node: Node):
        print(f"{node.value}")
    

