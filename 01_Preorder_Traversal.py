"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    #Write your code here
    if(root == None):
        return
    print root.data,
    #Comma after print in Python 2 implies that next print statment should continue on the same line
    #In Python 2, use print(root.data, end = '')
    
    preOrder(root.left)
    preOrder(root.right)
    
