def isPalindrome(s,l,r):
    s="abba"
    l=0
    r=len(s)-1
    if l>=r:
        return True
    if s[l] != s[r]:
        return False
       
    s[l],s[r] = s[r], s[l]
    return isPalindrome(s,l+1,r-1)
    
