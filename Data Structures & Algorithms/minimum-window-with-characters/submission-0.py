class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        s_count = {}
        t_count = {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)

        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]

            s_count[char] = 1 + s_count.get(char, 0)

            if char in t_count and s_count[char] == t_count[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                s_count[s[l]] -= 1

                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""
            

        

        

        
            
                


            
        

        return sub_str

                
                
        