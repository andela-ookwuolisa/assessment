def heap_sort(lst):
    n = len(lst)
     # bubble the max value to the top and sort the entire tree
    for i in range(n//2-1, -1, -1):
         heapify(lst, i, n)
    
    #puts the max value to the last index position
    for i in range(n-1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, 0, i)
    
    return lst
    
def heapify(lst, index, heap_size):
    largest_index = index
    l_child_index = (2 * index) + 1
    r_child_index = (2 * index) + 2

    if l_child_index < heap_size and lst[l_child_index] > lst[largest_index]:
        largest_index = l_child_index
    
    if r_child_index < heap_size and lst[r_child_index] > lst[largest_index]:
        largest_index = r_child_index
    
    if largest_index != index:
        lst[largest_index], lst[index] = lst[index], lst[largest_index]
        heapify(lst, largest_index, heap_size)

print(heap_sort([8,3,5,2,4]))
