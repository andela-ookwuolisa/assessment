'''
Linear search algorithm to return the index of an element in an array

Pseudocode
for(start to end of array)
{
    if (current_element equals to m)  
    {
        print (current_index);
    }
}
'''

def linear_search(arr, m):
    for index, element in enumerate(arr):
        if element == m:
            return index
    return -1

list_1 = list(range(15))
list_2 = list (range(0,30,2))

print(linear_search(['b','d','e','v','a','y'], 'a'))
print(linear_search(list_1,9))
print(linear_search(list_2,9))

