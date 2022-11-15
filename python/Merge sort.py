"""
Merge sort implementation
Recursion
"""

def merge_sort(list1):
    """
    Main merge sort function
    which performs the Divide and combine
    functions
    Base case is when the length of
    smallest list is 1(gets divided until its 1)
    """
    if(len(list1)<=1):
        return list1

    left_half,right_half = divide(list1)
    left=merge_sort(left_half)
    right=merge_sort(right_half)

    return combine(left,right)

def divide(list2):
    """
    Divides the list into two halves
    Takes a midpoint
    returns the seperated lists
    """

    mid=(len(list2))//2
    left=list2[:mid]
    right=list2[mid:]

    return left,right

def combine(left,right):

    """
    Combines the lists while comparing and sorting them
    returns the sorted and combined list
    """
    res=[]
    i=0
    j=0
    while(i<len(left) and j<len(right)):
        if(left[i]< right[j]):
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    #Following step is for 
    #when left half length higher then right half
    
    while(i<len(left)):
        res.append(left[i])
        i+=1
    
    #Following step is for 
    #when right half length higher then left half

    while(j<len(right)):
        res.append(right[j])
        j+=1

    return res

uslist=[30,1000,10,40,50,80]
sl=merge_sort(uslist)
print(sl)