from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for i in arr2: 
        arr1.append(i)
    return arr1


def pop_n(arr: List[int], n: int) -> List[int]:
    # n is greater than the arr size 
    if n + 1 > len(arr):  # assume 0 index. 5 means 6 elements here 
        return [] 
    # count from the last 
    index = len(arr) - n  # e.g last 2, len = 6, index 6 - 2 = 4 
    arr = arr[0:index] 
    # return the resulting list 
    return arr 
    

def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    # case: out of bound. insert at the end of the list 
    if index > len(arr): 
        arr.append(element)
        return arr 
    # assume 0 index here. 
    return arr[0:index] + [element] + arr[index:]


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
