def is_unique(string):
    return len(set(string)) == len(string)

def is_unique_set(string):
    char_seen = set()

    for ch in string:
        if ch in char_seen:
            return False
        char_seen.add(ch)
    
    return True

def is_unique_dict(string):
    char_seen = dict()

    for ch in string:
        if char_seen[ch] == 1:
            return False 
        char_seen[ch] = 1 
    
    return True
