def isPalindrome(self, x: int) -> bool:
    rev = str(x)
    if str(x) == rev[::-1]:
        return True
    else:
        return False
        