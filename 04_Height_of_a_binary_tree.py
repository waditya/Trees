# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    ##Height of a tree is number of edges in the longest path from root to leaf node
    ##Depth of a node is the number of edges between the node and the root node
    
    ##Height of a root is the maximum(height of left subtree, height of right subtree)
    if (root == None):
        return -1
    heightOfLeftsubtree = height(root.left)
    heightOfRightsubtree = height(root.right)
    return max(heightOfLeftsubtree,heightOfRightsubtree) + 1
