class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]

        s = s.lower()
        for i in s:
            if i not in l:
                s = s.replace(i,"")
        s1 = s[::-1]

        print(s)
        print(s1)

        if s == s1:
            return True
        else:
            return False