def binary_search(data, target):
  if len(data)==0:
    return False
  else:
    mid = len(data)//2
    if target == data[mid]:
      return True
    elif target > data[mid]:
      return binary_search(data[mid+1:],target)
    else:
      return binary_search(data[:mid],target)

data = [1,2,3,4,5,6]
print(binary_search(data,3))

