#Quick sort implementation
#Recursion


def quick_sort(list1):

    #Base case
    if(len(list1)<=1):
        return list1

    pivot=list1[0]
    #For the numbers smaller than pivot
    smaller_than_pivot=[]    
    #For the numbers greater than pivot   
    greater_than_pivot=[]

    #For loop for comparing each element with pivot
    #and adding it to respective list
    for i in range(1,len(list1)):
        if list1[i]<=pivot:
            smaller_than_pivot.append(list1[i])
        
        else:
            greater_than_pivot.append(list1[i])

    return quick_sort(smaller_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


print("Enter the number of elements in the list")
n=int(input())
unsorted=[]
for i in range(0,n):
    print("Enter the element one by one")
    x=int(input())
    unsorted.append(x)

#unsorted=[10,5,1,4,20,30]
print("Here's the sorted list using quick sort:")
print (quick_sort(unsorted))