"""
worse case scenario: O(n^2)
best case scenario (a sorted list): O(n)

Other quadratic sorts:
selection sort
insertion sort
"""

def bubble_sort(lst):
    for i in range(len(lst)-1):
        made_swap = False
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                made_swap = True
        if not made_swap:
            break