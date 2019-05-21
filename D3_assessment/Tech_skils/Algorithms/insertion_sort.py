def insertion_sort(lst):
    for index in range(1, len(lst)):
        while index > 0 and lst[index - 1] > lst[index]:
            lst[index - 1],  lst[index] = lst[index], lst[index - 1]
            index -= 1
    return lst

nums = [7,2,5,1,29,6,4,19,11]
print(insertion_sort(nums))
