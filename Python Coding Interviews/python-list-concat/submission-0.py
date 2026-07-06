from typing import List


def combine_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    new_lst = [] 
    for element in arr1 + arr2: 
        new_lst.append(element)
    return new_lst



# do not modify below this line
arr1 = [1, 3, 5]
arr2 = [4, 6, 8]

print(combine_elements(arr1, arr2))
print(arr1)
print(arr2)
