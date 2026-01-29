def isPalindrome(s):
    s = ''.join([char for char in s if char.isalnum()]).lower()
    if not s:
        return True

    l, r = 0, len(s) - 1

    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
