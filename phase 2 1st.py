"""class Student:
          def __init__(self,name,rollno,javamarks,pythonmarks,mathmarks):
                  self.name=name
                  self.rollno=rollno
                  self.javamarks=javamarks
                  self.pythonmarks=pythonmarks
                  self.mathmarks=mathmarks

obj1=Student("aman",501,67,45,87)
print(obj1.name)
print(obj1.rollno)
print(obj1.javamarks)
print(obj1.pythonmarks)
print(obj1.mathmarks)     
obj2=Student("shaheyda",98,78,98,57)
print(obj2.name)
print(obj2.rollno)
print(obj2.javamarks)
print(obj2.pythonmarks)
print(obj2.mathmarks)
obj3=Student("shahanaz",456,89,96,78)
print(obj3.name)
print(obj3.rollno)
print(obj3.javamarks)
print(obj3.pythonmarks)
print(obj3.mathmarks)


class student:
          def __init__(self,name,rollno,section,rank):
                  self.name=name
                  self.rollno=rollno
                  self.section=section
                  self.rank=rank
          def printAllDetails(self):
                  print(self.name)
                  print(self.rollno)
                  print(self.section)
                  print(self.rank)
obj=student("shaheyda","s8",5,9)
obj.printAllDetails()      
obj2=student("shahanaz",45,7,4)
obj2.printAllDetails()                   


class node:
          def __init__(self,data):
                  self.data=data
                  self.next=None
obj1=node(71)
obj2=node(72)  
obj3=node(73)
obj4=node(74)
obj5=node(75)
obj6=node(76)
obj7=node(77)
obj8=node(78)
obj9=node(79)
obj10=node(80)
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
obj7.next=obj8
obj8.next=obj9
obj9.next=obj10
currentNode=obj1
while currentNode != None:
    print(currentNode.data, end =  --> ")
    currentNode = currentNode.next """


"""class node:
          def __init__(self,data):
                  self.data=data
                  self.next=None

def insertAtHead(head,ele):
          temp=Node(ele)
          temp.next = head
          return temp"""

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
 
def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head

 
"""# Task - 1
def insertAtHead(head, ele):
    temp = Node(ele)
    temp.next = head 
    return temp"""



def deleteTailNode(head):
          if head == None or head.next == None:
                  return home
          previous = None
          currentNode=head
          while currentNode.next != None:
                  previous = currentNode
                  currentNode = currentNode.next
          previous.next = None
          return head  
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAtTail(head, ele)
print("Final linked list is:")
printLinkedList(head)      
              
 

##deletetion of tail node

def deleteHeadNode(head):
     if head == Node:
          return head
     secondNode = head.next
     head.next = None
     return secondNode