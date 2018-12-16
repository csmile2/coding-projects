"""
MCS275 - Project2 - 11/5/2018
By Clayton Smiley
Build and Traverse a Ternary Tree
"""


#  define the Tree class with init, insert and traverse methods
class Tree(object):

    #  node starts with None types as it's r, l and middle values
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.middle = None


    # appends a new node to the ternary tree
    def insert_node(self, new_value):
        if new_value < self.value:
            if self.left == None:
                self.left = Tree(new_value)
            else:
                self.left.insert_node(new_value)
        elif new_value == self.value:
            if self.middle == None:
                self.middle = Tree(new_value)
            else:
                self.middle.insert_node(new_value)
        else:
            if self.right == None:
                self.right = Tree(new_value)
            else:
                self.right.insert_node(new_value)

    #  prints out the ternary tree vals in postorder
    def traverse_LMRW(self):

        if self.left != None:
            self.left.traverse_LMRW()
        if self.middle != None:
            self.middle.traverse_LMRW()
        if self.right != None:
            self.right.traverse_LMRW()
        print(self.value)


#  helper fn to build the nodes of ternary tree given a passed list of values
def construct_ternary_tree(L):
    T = Tree(L[0])
    for value in L[1:]:
        T.insert_node(value)

    return T


def main():
    #  starting list of nodes we'd like to construct ternary tree with
    L = [4, 1, 2, 2, 3, 1, 0, 4, 6, 5, 6, 4]
    Ternary_Tree = construct_ternary_tree(L)
    Ternary_Tree.traverse_LMRW()

main()
