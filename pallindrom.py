class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_cleaned = ''
    
        for i in s:
            if i.isalnum()==True:
                s_cleaned += i
        
        s1 = s_cleaned[::-1]

        return s1 == s_cleaned