#Name : Manohar Prepalli
#Assignement: week_9
# Title : Algorithem for Merge sort
# github link : https://github.com/parepallil/week_9.git


#program starts from hear.
# Part One: Merge Sort
def merge_sort(arr):#creating function to now the length of array.
    
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Sorting each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merging the sorted halves
    return merge(left_half, right_half)

def merge(left_half, right_half):#creating function for right and left half
    merged_result = []
    left_idx = right_idx = 0

    # Merging process by while loop
    while left_idx < len(left_half) and right_idx < len(right_half):
        
        if left_half[left_idx] < right_half[right_idx]:
            merged_result.append(left_half[left_idx])
            left_idx += 1
            
        else:
            merged_result.append(right_half[right_idx])
            right_idx += 1

    # Appending remaining elements (if any)
    merged_result.extend(left_half[left_idx:])
    merged_result.extend(right_half[right_idx:])

    return merged_result

# Part Two: Handling Descending Order
def merge_sort_descending(arr):#creating the function for to print in descending order.

    if len(arr) <= 1:

        return arr

    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    left_half = merge_sort_descending(left_half)
    right_half = merge_sort_descending(right_half)

    return merge_descending(left_half, right_half)

def merge_descending(left_half, right_half):

    merged_result = []
    left_idx = right_idx = 0

    while left_idx < len(left_half) and right_idx < len(right_half):
        
        if left_half[left_idx] > right_half[right_idx]:  # Changed comparison for descending order
            merged_result.append(left_half[left_idx])
            left_idx += 1
        else:
            merged_result.append(right_half[right_idx])
            right_idx += 1

    merged_result.extend(left_half[left_idx:])
    merged_result.extend(right_half[right_idx:])

    return merged_result

# Step 2: Implement Merge Sort iteratively (without using recursion)
def iterative_merge_sort(arr):
    stack = [(0, len(arr))]
    result = arr.copy()

    while stack:
        start, end = stack.pop()

        if end - start <= 1:
            continue

        mid = (start + end) // 2

        stack.append((start, mid))
        stack.append((mid, end))

        result[start:end] = merge_descending(result[start:mid], result[mid:end])

    return result

n=int(input("Enter size of array :"))#takeing the input
a=[]

for i in  range(n):#for loop to iterate the elements.
    a.append(int(input("Enter input element :")))
print(merge_sort(a))
print(merge_sort_descending(a))
