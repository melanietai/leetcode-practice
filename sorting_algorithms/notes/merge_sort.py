"""
Fastest possible runtime to sort a list is O(n log n)
- n becasue you have to touch every item in the list once
- log n because the best possible strategy is divde and conquer method (merge and Quicksort use)
"""

# merge two sorted arrays

def merge(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    
    if lst1[0] < lst2[0]:
        cur = lst1.pop(0)
    else:
        cur = lst2.pop(0)

    return [cur] + merge(lst1, lst2)


if __name__ == '__main__':
    lst1 = [1, 3]
    lst2 = [2, 4, 5]

    print(merge(lst1, lst2))


def make_merge(lst1, lst2):
    ans = []
    lst1 = lst1[::-1]
    lst2 = lst2[::-1]

    while lst1 or lst2:
        if not lst1:
            ans.append(lst2.pop())
        elif not lst2:
            ans.append(lst1.pop())
        elif lst1[-1] < lst2[-1]:
            ans.append(lst1.pop())
        else:
            ans.append(lst2.pop())
    return ans

def merge_sort(lst):
    if len(lst) < 2:
        return lst
    
    mid = int(len(lst) / 2)

    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])

    return merge(lst1, lst2)

if __name__ == '__main__':
    lst1 = [1, 3]
    lst2 = [2, 4, 5]

    print(make_merge(lst1, lst2))

    lst3 = [1, 3]
    lst4 = [2, 4, 5]
    print(merge(lst3, lst4))

    lst = [2, 1, 7, 4, 5, 3, 6, 8]
    print(merge_sort(lst))

