class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        self.anagram_groups = {}
        
        for i in strs:
            sorted_word = ''.join(sorted(i))
            if sorted_word in self.anagram_groups:
                self.anagram_groups[sorted_word].append(i)
            else:
                self.anagram_groups[sorted_word] = [i]

        return list(self.anagram_groups.values())#,self.anagram_groups

# Create an instance of the Solution class
solution_instance = Solution()

# Test cases
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution_instance.groupAnagrams(strs1))

strs2 = [""]
print(solution_instance.groupAnagrams(strs2))

strs3 = ["a"]
print(solution_instance.groupAnagrams(strs3))
