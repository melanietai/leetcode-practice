def quicksort(lst):
    if len(lst) < 2:
        return lst  
    
    mid = int(len(lst) / 2)
    pivot = lst[mid]

    lo, eq, hi = [], [], []
    for n in lst:
        if n < pivot:
            lo.append(n)
        elif n == pivot:
            eq.append(n)
        else:
            hi.append(n)
    
    return quicksort(lo) + eq + quicksort(hi)
