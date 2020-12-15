
def isPalindrome( x: int) -> bool:

    if x<0:
        return False

    temp, y = int()

    res = x
    while res !=0:
        temp = res%10
        y=y*10+temp
        res=int(res/10)

    return x==y
