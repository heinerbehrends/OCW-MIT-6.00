def isPalindrome(s):
    """Return True if s is a palindrome and False otherwise."""
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

if isPalindrome("regallager") == True:
    print True

def isPalindrome1(s, indent):
    """Return True if s is a palindrome and False otherwise."""
    print indent, "isPalindrome called with", s
    if len(s) <= 1:
        print indent, "About to return True from base case"
        return True
    else:
        ans = s[0] == s[-1] and isPalindrome1(s[1:-1], indent + indent)
        print indent, "about to return", ans
        return ans

isPalindrome1("regallager", " ")
    
