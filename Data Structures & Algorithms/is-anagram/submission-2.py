class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        for c in s:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1

        print(char_count)

        
        for c in t:
            if c in char_count:
                char_count[c] -= 1

        print(char_count)

        for c in char_count:
            if char_count[c] != 0:
                return False
        
        return True
      