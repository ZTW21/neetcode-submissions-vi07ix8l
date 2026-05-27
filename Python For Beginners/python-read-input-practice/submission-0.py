def add_two_numbers() -> int:
    user_in = input()
    strings = user_in.split(",")
    ints = []
    for s in strings:
        ints.append(int(s))

    return sum(ints)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
