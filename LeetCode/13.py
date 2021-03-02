
def romanToInt( s: str) -> int:

    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    res = 0
    for i, element in enumerate(s):

        if i<len(s)-1 and a[element]<a[s[i+1]]:
            res -= a[element]
        else:
            res += a[element]
    return res
