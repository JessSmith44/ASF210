def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        # line 5-7 we are splitting the list/array in half, setting the mid point and sides 
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        # print(lefthalf, 'line 8')
        # print(righthalf, 'line 9')

        # not gonna lie, over thought this and had many issues figuring out why 
        # my merge was not working as expected. Upon further inspection I realized I was attempting 
        # to create the merge inside the mergeSort function rather than call it. Once I fixed that and 
        # simply called the merge function while passing in the values needed Everything ran much better.
        mergeSort(lefthalf)
        mergeSort(righthalf)
        # lines 15 and 16 are passing both sides through the mergeSort function to split them repeatedly until
        # one value remains
        merge(nlist, lefthalf, righthalf)
        # Line 19 is calling the merge function and passing the needed values to it so that everything can be 
        # merged and sorted.
 
    print("Merging ",nlist)

def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    # print(nlist, lefthalf, righthalf, 'line 31')
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1
        # print(lefthalf, 'line 41')

    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
        # print(righthalf, 'line 57')
    return nlist

nlist = [ 55 ,  31 ,  26 ,  20 ,  63 ,  7 ,  51 ,  74 ,  81 ,  40 ]
# print(nlist, 'line 58')
mergeSort(nlist)
print(nlist, 'line 62')


# Please pardon all the print statements, I use them to help me see what all is going on. As per personal preference
# I prefer to leave them in so I can see my process in later assignments to help me debug issues along the way. 