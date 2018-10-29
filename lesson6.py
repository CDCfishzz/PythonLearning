def trim(s):
    while len(s) != 0 and s[0] == " ":
        s = s[1:]
    while len(s) != 0 and s[-1] == " ":
        s = s[:-1]
    return s


def find_min_and_max(l):
    if len(l) == 0:
        return None, None
    min_l, max_l = l[0], l[0]
    for x in l:
        if min_l > x:
            min_l = x
        if max_l < x:
            max_l = x
    return min_l, max_l



