import time
import random

def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partitionStart(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
        

def partitionStart(a_list, start, end):
    return partition(a_list, start, end)

def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot = a_list[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            # Swap the values
            a_list[low], a_list[high] = a_list[high], a_list[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    # Swap the values
    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high


print("Quick Sort:")
#myList = [54,26,93,17,77,31]
myList = [x for x in range(1000)]
random.shuffle(myList)

#print(myList)
start_time = time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()
#print()
#print("Sorted Listed: ")
# print(myList)   

print(f"The execution time is: {end_time-start_time}")


###########
# sort by last element 


def quickSort2(sequence):
    length = len(sequence)
    if length <=1:
        return sequence
    else:
        pivot = sequence.pop()
        # print(pivot, "line 81")
    
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quickSort2(items_lower) + [pivot] + quickSort2(items_greater)


start_time = time.time()
sequence = [x for x in range(1000)]
random.shuffle(sequence)
# [5,2,6,7,15,635,221,634,45,6,37,9,8]
quickSort2(sequence)
end_time = time.time()
print(f"The execution time is: {end_time-start_time}")


###########
# sort by middle element

def qsort(a, low, hi):
    if(low >= hi):
        return
    p = a[(low + hi) // 2]       
    i = low - 1
    j = hi + 1
    while(1):
        while(1):              
            i += 1
            if(a[i] >= p):
                break
        while(1):               
            j -= 1
            if(a[j] <= p):
                break
        if(i >= j):
            break
        a[i],a[j] = a[j],a[i]
    qsort(a, low, j)
    qsort(a, j+1, hi)
    return(qsort)
    


start_time = time.time()
a = [x for x in range(1000)]
random.shuffle(a)
# [11,5,6,35,245,86,91,307,74,4,3]
qsort(a, 0, len(a)-1)
end_time = time.time()
# print(a)
print(f"The execution time is: {end_time-start_time}")


#########
# sort by random element
# With several run throughs the random selection for a pivot point seems to give the 
# best lowest timeframe upon return. selecting the first index and the last have switched between
# being lower than the other per run, while using the middle index has the highest time return of 
# the four per run.

def randQuickSort(list):
    def sorting(first, l, r):
        if r <= l:
            return
        pivot_index = random.randint(l,r)

        first[l], first[pivot_index]= first[pivot_index], first[l]

        i = l
        for j in range(l+1, r+1):
            if first[j]< first[l]:
                i +=1
                first[i], first[j] = first[j], first[i]

        first[i], first[l] = first[l], first[i]

        sorting(first, l, i-i)
        sorting(first, i+1, r)
    if list is None or len(list) < 2 :
        return
    sorting(list, 0, len(list)-1)


start_time = time.time()
list = [x for x in range(1000)]
random.shuffle(list)
# [11,5,6,35,245,86,754,0,68]
randQuickSort(list)
end_time = time.time()
# print(list)
print(f"The execution time is: {end_time-start_time}")