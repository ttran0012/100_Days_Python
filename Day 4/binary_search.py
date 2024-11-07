# Binary Search

# if we got an a array that is sorted
# ex, [1,2,3,4,5,6,7,8,9]


def binar_search(arr, item):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        # guess = arr[mid]
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            right = mid - 1
        else:
            left = mid + 1

    return None


my_arr = [1,2,3,4,5,6,7,8]

print(binar_search(my_arr, 5))