# Use stack
def isPalindrome(s:str):
    stack = []
    p = 0
    mid = int(len(s)/2)

    if len(s)%2==0: p = mid
    else: p = mid + 1

    for i in range(0, mid):
        stack.append(s[i])
    for i in range(p, len(s)):
        if s[i] != stack.pop():
            return False
    return True

print(isPalindrome("babcycbab"))