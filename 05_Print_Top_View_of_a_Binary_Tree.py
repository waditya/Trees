"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root):
  #Write your code here
    node = root
    print node.data,
  #Print all the left node side of the root node
  #Point Node to left node
  #Print until the node is None
    node = root.left
    while(node!=None):
        print node.data,
        node = node.left
        
  #Point Node to right node
  #Print until the node is None
    node = root.right
    while(node!=None):
        print node.data,
        node = node.right
    
