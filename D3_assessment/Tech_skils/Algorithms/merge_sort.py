def merge_sort(lst):
    if len(lst) < 2 :
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    return result + left + right

nums = [7,2,5,1,29,6,4,19,11]
print(merge_sort(nums))
