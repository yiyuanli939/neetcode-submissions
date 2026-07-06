from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    new_lst = [] 
    index = -1 
    while(index >= -len(arr)): 
        new_lst.append(arr[index])
        index -= 1 
    return new_lst 

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
