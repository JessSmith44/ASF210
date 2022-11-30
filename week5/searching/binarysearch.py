def binary_recursive(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return True
        # binary_recursive(arr, elem, start, mid-1)
    # elem > arr[mid]
    return False
    # binary_recursive(arr, elem, mid+1, end)

array = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

print(binary_recursive(array,31))
print(binary_recursive(array,77))

array = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

print(binary_recursive(array, "Delta"))






# def binary_recursive(array, val):
#     if val < array[0] or val > array[-1]:
#         return False
#     mid = len(array) // 2
#     left = array[:mid]
#     right = array[mid:]
#     if val == array[mid]:
#         return True
#     elif array[mid] > val:
#         return binary_recursive(left, val)
#     elif array[mid] < val:
#         return binary_recursive(right, val)
#     else:
#         return False