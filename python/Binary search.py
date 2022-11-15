#Binary search implementation
#Using iterative approach

def binary_search(list1,target):
    first=0
    last=len(list1)-1
    found=0
    while(first<=last and found==0):

        mid=(first+last)//2

        if(list1[mid]==target):
            found=1
            print("Element found at index:",mid)
            return
        
        elif(list1[0]==target):
            found=1
            start=0
            print("Element found at index",start)
            return
        
        elif(list1[-1]==target):
            found=1
            end=-1
            print("Element found at index",end)
            return

        elif(target>list1[mid]):
            first=mid+1

        else:
            last=mid-1

    print("Target element not found")
    return 

import time
start_time = time.time()
print("\nEnter the number of elements")
n=int(input())
#list1=[2,3,4,5,6]
#target=2
list1=list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
print("\nEnter the element to find:")
target=int(input())
binary_search(list1,target)
print("Process finished --- %s seconds ---" % (time.time() - start_time))

