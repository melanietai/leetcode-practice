def is_permutation_counter(s1, s2):
    def counter(s):
        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
        
        return counter 
    
    if len(s1) != len(s2):
        return False 
    
    return counter(s1) == counter(s2)
