

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = [0] * 26  # Array to hold character counts for string s
        t_count = [0] * 26  # Array to hold character counts for string t

        for char in s:
            s_count[ord(char) - ord('a')] += 1

        for char in t:
            t_count[ord(char) - ord('a')] += 1
        
        return s_count == t_count
    print(isAnagram("anagram", "nagaram"))  # Output: True
    print(isAnagram("rat", "car"))# Output :False

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        self.s_count={}
        self.t_count={}
        for char in s:
            if char in self.s_count.keys():
                self.s_count[char]+=1
            else:
                self.s_count[char]=1

        for char in t:
            if char in self.t_count.keys():
                self.t_count[char]+=1
            else:
                self.t_count[char]=1
        
        if self.s_count==self.t_count:
            return True
        else:
            return False 
        

    print(isAnagram("anagram", "nagaram"))  # Output: True
    print(isAnagram("rat", "car"))# Output :False