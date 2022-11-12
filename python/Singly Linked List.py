# Python program to
# demonstrate Linked List implementation

#We created a Node class to use
#whenever we need to create a new node

from time import sleep

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    #Print the Linked List
    def print(self):
        n=self.head
        if n is None:
            print("Linked List is empty!")
        else:
            #n=self.head 
            while(n is not None):
                print(n.data, "--->",end=" ")
                n=n.next
            sleep(2)
            return
            

    #Function to add a node to the beginning
    #of Linked List
    def add_begin(self,data):
        n1=Node(data)
        n1.next=self.head
        self.head=n1

    #Function to add a node to the end
    # of Linked List
    def add_end(self,data):
        new_node=Node(data)
        n=self.head
        if n is None:
            self.head=new_node
        else:
            while n.next is not None: 
                n=n.next
            n.next=new_node

    #Function to add a node(data) after
    #the given element x
    def add_after(self,data,x):
        #find x
        #compare each data item
        n=self.head
        while(n is not None):
            if(n.data==x):
                break
            n=n.next
        #The while loop breaks in two conditions
        #One when it reaches the end of list and hasn't found the element
        #Other when it finds the element
        #in n.data(n's data field)
        if n is None:
            print("Node not found in Linked List")
            
        else:
            new_node=Node(data)
            new_node.next=n.next
            n.next=new_node
    
    #Function to add a node(data) before
    #the given element x
    def add_before(self,data,x):

        n=self.head
        #Checking if the list is empty
        if(n is None):
            print("Linked List is empty!")
            return
        
        #If the element to be added before
        #is the first one
        #meaning if Linked list
        #contains only one element
        elif(n.data==x):
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
            return
        
        else:
            n=self.head
            while(n.next is not None):
                if((n.next).data==x):
                    break
                n=n.next
            #The while loop breaks in two conditions
            #One when it reaches the end of list and hasn't found the element
            #Other when it finds the element in the next node
            #and itself is n
            if (n.next is None):
                print("Node not found in Linked List")
            else:
                new_node=Node(data)
                new_node.next=n.next
                n.next=new_node

    #Function to add delete
    #the element at beginning
    def del_begin(self):
        n=self.head

        if(n is None):
            print("Linked List is empty!")
       
        else:
            self.head=n.next

    #Function to add delete
    #the element at end
    def del_end(self):
        n=self.head

        if(n is None):
            print("Linked List is empty!")

        elif(n.next is None):
            self.head=n.next
            
            
        else:   
            while((n.next).next is not None):
                n=n.next
            n.next=None

    #Function to add delete
    #the node x
    def del_val(self,x):
        n=self.head
        if(n is None):
            print("Linked List is empty!")
        elif(n.data == x):
            self.head=n.next

        else:
            while(n.next) is not None:
                if(n.next.data==x):
                    break
                n=n.next
            #The while loop breaks in two conditions
            #One when it reaches the end of list and hasn't found the element
            #Other when it finds the element in the next node
            #and itself is n
            if n.next is None:
                print("Element Not found")
            
            else:
                n.next=(n.next).next




#Driver Code

ll1=LinkedList()
#ll1.print()
#ll1.add_begin(100)
#ll1.add_begin(200)
#ll1.add_begin(300)
#ll1.del_val(300)
#ll1.del_end()
#l1.add_begin(200)
#ll1.add_begin(300)
#ll1.add_after(200,100) 
#ll1.add_before(10,200)
#ll1.del_begin()
#ll1.add_end(1000)
#ll1.add_after(200,100)
flag=0
while(flag==0):
    #User input
    print("\nSelect an operation to perform on Linked List")
    print("1. Add a node to the beginning of list")
    print("2. Add a node to the end of list")
    print("3. Add a node after a provided node")
    print("4. Add a node before a provided node")
    print("5. Delete the node at the beginning")
    print("6. Delete the node at the end")
    print("7. Delete the provided node")
    print("8. Print the Linked List")
    print("9. Exit")
    uc=int(input())
    if(uc==1):
        print("Enter the value to be added")
        data=input()
        ll1.add_begin(data)
    elif(uc==2):
        print("Enter the value to be added")
        data=input()
        ll1.add_end(data)
        #flag=1
    elif(uc==3):
        print("Enter the value to be added")
        data=input()
        print("Enter the node after which the value is to be added")
        x=input()
        ll1.add_after(data,x)
    elif(uc==4):
        print("Enter the value to be added")
        data=input()
        print("Enter the node before which the value is to be added")
        x=input()
        ll1.add_before(data,x)
    elif(uc==5):
        ll1.del_begin()
    elif(uc==6):
        ll1.del_end()
    elif(uc==7):
        print("Enter the value/node to be deleted")
        data=input()
        x=input()
        ll1.del_val(data)
    elif(uc==8):
        ll1.print()
    elif(uc==9):
        flag=1
    else:
        print("Invalid choice, please select a valid operation")
quit()
        
        