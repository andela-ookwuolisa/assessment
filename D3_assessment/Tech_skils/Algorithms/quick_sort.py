def quick_sort(lst):
    if len(lst)<2:
        return lst
    else:
        pivot = lst[0]
        greater = [element for element in lst[1:] if element > pivot]
        lesser = [element for element in lst[1:] if element <= pivot]
        return quick_sort(greater) + [pivot] + quick_sort(lesser)


nums = [7,2,5,1,29,6,4,19,11]
print(quick_sort(nums))
