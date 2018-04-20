import string

def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        letter = ''
        for c in s:
            if c in string.ascii_lowercase:
                letter += c
        return letter
    
    def isPal(s):
        print("isPal called with " + s)
        if len(s) <=1 :
            print("About to return True from base case")
            return True
        else:
            answer = s[0]==s[-1] and isPalindrome(s[1:-1])
            print(" About to return', answer, for " + s)
            return answer
    return isPal(toChars(s))
    
def testIsPalirome() :
    print("Try abcba")
    print(isPalindrome("abcba"))
    print("Try doGood")
    print(isPalindrome("doGood"))

testIsPalirome()