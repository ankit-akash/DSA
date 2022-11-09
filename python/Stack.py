# Python program to
# demonstrate stack implementation
# using collections.deque
 
from collections import deque
# To add a delay between
# print statements and next steps
from time import sleep
 

class stack():
    def __init__(self):
        self.stack=deque()
    
    # Push into stack operation

    def push(self):
        print("Enter the element to be pushed:")
        item=int(input())
        self.stack.append(item)
        #stack.mainscreen(self)

    # Popping the top element of stack

    def remove(self):
        if(len(self.stack)==0):
            print("Cannot pop from an empty stack\n")
            sleep(2)
            return
        else:
            x=str(self.stack.pop())
            print (str("Popped the element:" + " " + x + "\n"))
            sleep(2)
            return

    # Displays the topmost element of the stack

    def top(self):
        if(len(self.stack)==0):
            print("Empty stack")
            sleep(2)
            return
        else:  
            t=self.stack[-1]
            print (str("The top element:" + " " + t + "\n"))
            sleep(2)
            return
        
    #prints the complete stack

    def display(self):
        if(len(self.stack)==0):
            print("Empty stack")
            
        
        else:
            print(self.stack)
            
        sleep(2)
        return

# Driver code        
s1=stack()
flag=0

# A while loop to keep the main menu screen running
#This exits when user chooses exit option
while(flag==0):
    # User input
    print("Select an operation to perform on stack")
    print("1. Push element")
    print("2. Pop element")
    print("3. Print stack")
    print("4. Display top/peek elemnt")
    print("5. Exit")
    uc=int(input())
    if(uc==1):
        s1.push()
    elif(uc==2):
        s1.remove()
        #flag=1
    elif(uc==3):
        s1.display()
    elif(uc==4):
        s1.top()
    else:
        flag=1
quit()


 
