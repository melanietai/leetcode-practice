def replace_space(s, l):
    new_s = ""

    for i in range(l):
        if s[i] != " ":
            new_s += s[i]
        else:
            new_s += "%20"   
    return new_s 

def reverse_remove_space(s, l):
    ch_list = list(s)
    new_i = len(ch_list)

    for i in reversed(range(l)):

        if ch_list[i] == " ":
            ch_list[new_i - 3 : new_i] = "%20"
            new_i -= 3
        else:
            ch_list[new_i - 1] = ch_list[i]
            new_i -= 1
    return "".join(ch_list)

if __name__ == "__main__":
    s = "Mr John Smith    "
    l = 13
    expected = "Mr%20John%20Smith"
    result = replace_space(s, l)
    print(result == expected)

    ans = reverse_remove_space(s, l)
    print(ans == expected)