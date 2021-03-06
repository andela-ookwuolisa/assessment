from random import randint
def quick_sort(lst, start, end):
    if start < end:
        pivot = randint(start, end)
        lst[end], lst[pivot] = lst[pivot], lst[end]
        split = partition(lst, start, end)
        quick_sort(lst, start, split-1)
        quick_sort(lst, split+1, end)

def partition(lst, start, end):
    pivot_index = start-1
    for index in range(start, end):
        if lst[index] < lst[end]:
            pivot_index = pivot_index +1
            lst[pivot_index], lst[index] = lst[index], lst[pivot_index]
    lst[pivot_index+1], lst[end] = lst[end], lst[pivot_index+1]
    return pivot_index+1

nums = [7,2,5,1,29,6,4,19,11]
quick_sort(nums,0, len(nums)-1)
print(nums)
