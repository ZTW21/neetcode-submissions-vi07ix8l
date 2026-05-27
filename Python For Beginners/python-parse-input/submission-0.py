from typing import List

def read_integers() -> List[int]:
    user_list = input()
    arr = user_list.split(",")

    int_list = []
    for i in arr:
        int_list.append(int(i))

    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
