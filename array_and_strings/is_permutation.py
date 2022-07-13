def is_permutation_counter(s1, s2):
    def counter(s):
        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
        
        return counter 
    
    if len(s1) != len(s2):
        return False 
    
    return counter(s1) == counter(s2)

def is_permutation_sort(s1, s2):
    if len(s1) != len(s2):
        return False

    sorted_s1, sorted_s2 = sorted(s1), sorted(s2)

    for i in range(len(s1)):
        if sorted_s1[i] != sorted_s2[i]:
            return False 

    return True

def is_permutation_bytearray(s1, s2):
    if len(s1) != len(s2):
        return False 

    array_counter = [0] * 256

    for ch in s1:
        array_counter[ord(ch)] += 1
    
    for ch in s2:
        if array_counter[ord(ch)] == 0:
            return False 
        array_counter[ord(ch)] -= 1 
    
    return True
