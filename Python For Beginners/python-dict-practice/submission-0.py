from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    output = {}
    for c in word:
        output[c] = output.get(c, 0) + 1 
    return output



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
