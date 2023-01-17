#  File: ExpressionTree.py

# Description: evaluates a mathematical expression and represents it as a prefix and postfix expression tree

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        current=Node()
        stack=Stack()
        self.root=current
        list=expr.split()

        for i in range(len(list)):
            if list[i]=="(":                # if left parenthesis, create left child and push parent onto stack
                temp=Node()
                current.lChild=temp
                stack.push(current)
                current=temp
            elif list[i]==")":              # if right parenthesis, pop stack
                current=stack.pop()
            elif list[i] in operators:      # if operator, assign node data, push onto stack, and create right child
                current.data=list[i]
                stack.push(current)
                temp=Node()
                current.rChild=temp
                current=temp
            else:                           # if operand, assign node data and pop stack
                current.data=list[i]
                current=stack.pop()
    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if aNode==None:return 0.0

        if aNode.data in operators:         # if operator, evaluate expression of children
            left=self.evaluate(aNode.lChild)
            right=self.evaluate(aNode.rChild)
            return eval(f"{left}{aNode.data}{right}")

        return float(aNode.data)            # if operand, return data
    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        str=f"{aNode.data} "
        if aNode.lChild!=None:              # as long as aNode has children, run through tree left children first, right children next
            str+=self.pre_order(aNode.lChild)
            str+=self.pre_order(aNode.rChild)
        return str

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        str=f"{aNode.data} "
        if aNode.lChild!=None:              # as long as aNode has children, run through tree right children first, going backwards up tree
            str=self.post_order(aNode.rChild)+str
            str=self.post_order(aNode.lChild)+str
        return str

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
