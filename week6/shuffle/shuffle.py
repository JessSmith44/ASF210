from random import randint 
import time

def shuffleList(arr):
    n =len(arr)

    for i in range(n):
        # random index
        rand = randint(i, n -1)
        # switch elements
        arr[i], arr[rand] = arr[rand], arr[i]

    return arr
print("Before shuffle:")
print([7, 20, 26, 31, 40, 51, 55, 63, 74, 81])

start_time = time.time()
print("After shuffle:")
print(shuffleList([7, 20, 26, 31, 40, 51, 55, 63, 74, 81]))

end_time = time.time()
print(f"the end time is: {end_time-start_time}")

# I am not sure how to resolve exactly what the time complexity is for this, I know the run time and have that
# displaying. From what I understand the time complexity for this is O(n) although I am not 100% on this. 