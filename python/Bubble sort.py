#Bubble sort

def bubble_sort(list1):
    swap=1
    for i in range(0,len(list1)-1):
        #The if condition stops further passes
        #When all the list is already sorted
        if(swap==0):
            print("The sorted list:\n",list1)
            return    
        swap=0
        for j in range(0,len(list1)-1):
            if(list1[j]>list1[j+1]):
                list1[j],list1[j+1]=list1[j+1],list1[j]
                swap=1
                #print(list1)
                


    print("The sorted list:\n",list1)
    return


#list1 = [10,4,5,6,7]
print("Enter the number of elements you want")
n=int(input())
list1=list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
bubble_sort(list1)

