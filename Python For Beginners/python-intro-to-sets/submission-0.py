from typing import List, Set # this adds type hints for List and Set

def list_to_set(nums: List[int]) -> Set[int]:
    _set = set(nums)
    return _set
    

# do not modify below this line
print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))
