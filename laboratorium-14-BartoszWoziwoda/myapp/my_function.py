from typing import List

def bubblesort(lst: List) -> List:
    done = False
    while done is not True:
        done = True
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                done = False
    return lst