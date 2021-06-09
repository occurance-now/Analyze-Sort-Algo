def combine_list(arr1, arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr

def mergesort(arr):
    if len(arr) < 2:
        return arr[:]

    else:
        middle = len(arr)//2
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return combine_list(l1, l2)

#l = [6,8,1,4,10,7,8,9,3,2,5]
#l = [8,6,2,5]
#print(divide_arr(l))

# l1 = [1,4,6,8]
# l2 = [2,3,5,7,8,9,10]

#print(f"Merged list: {merge_sorted(l1, l2)}")

#Steps
#1. Compare first element in each list and append smaller element
#2. Using a indices and an iterator perform same comparison for
#   all elements in both lists
#3. Move marker up by 1 position after smaller is found
#4. Copy remaining list once comparisons are complete and there
#   are items still remaining i one of the lists
