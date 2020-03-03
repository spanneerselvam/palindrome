def palindrome(w1):
    end = len(w1) - 1
    beg = 0
    while (end > beg):
        if w1[beg] != w1[end]:
            return False
        beg += 1
        end -= 1
    return True
print(palindrome("MOM"))
print(palindrome("MAM"))
print(palindrome("ANNA"))
print(palindrome("TRUE"))
print(palindrome("MOMA"))
print(palindrome("MOOM"))
