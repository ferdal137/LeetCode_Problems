class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t)!=len(s):
            return False
        else:
            s_letters = []
        
            for letter in s:
                s_letters.append(letter)

            for letter in t:
                if letter in s_letters:
                    s_letters.remove(letter)
                    pass
                else:
                    return False

            return True
    
