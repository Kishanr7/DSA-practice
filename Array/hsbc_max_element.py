def index_of_max_element(arr):
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index
# Example usage:
arr = [1, 3, 7, 0, 5]   
print(index_of_max_element(arr))  # Output: 2