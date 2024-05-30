"""class Node:
          def __init__(self,data):
                  self.data=data
                  self.left=None
                  self.right=None 

def printPreorder(root):
                  if root == None:
                          return
                  print(root.data, end = ", ")
                  printPreorder(root.left)
                  printPreorder(root.right)
def printInorder(root):
        if root == None:
                return
        printPreorder(root.left)
        print(root.data, end = ", ")
        printPreorder(root.right)
def printPostorder(root):
        if root == None:
                return
        
obj1 = Node(2)
obj2 = Node(7)
obj3=Node(2)
obj4=Node(6)
obj5=Node(5)
obj6=Node(11)
obj7=Node(5)
obj8=Node(9)
obj9=Node(4)

obj1.left=obj2
obj2.left=obj3
obj2.right=obj4
obj4.left=obj5
obj4.right=obj6
obj1.right=obj7
obj7.right=obj8
obj8.left=obj9

printPreorder(obj1)
print()
printInorder(obj1)
print()

def printLevelOrderTraversal(root):
    if root == None:
        return 
    Q = [root]
    result = []
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step-1 (Deleting)
            currNode = Q.pop(0)
 
            # step-2 (Appending to subResult)
            subResult.append(currNode.data)
 
            # step-3 (Enquing the left child)
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step-4 (Enquing the right child)
            if currNode.right != None:
                Q.append(currNode.right)
 
        result.append(subResult)    
 
        print(result)
 """

class Solution(object):
          def maxLevelSum(self,root):
                  if root == None:
                          return 0
                  Q=[root]
                  resultLevel = 0
                  resultSum = -1000000
                  currLevel = 1 
                  while len(Q)>0:
                          n=len(Q)
                          currSum=0
                          for i in range(n):
                                  currNode = Q.pop(0)
 
