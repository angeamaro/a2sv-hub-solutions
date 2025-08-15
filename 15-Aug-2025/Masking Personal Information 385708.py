# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        s = s.strip()
        
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')
            return f"{name[0]}*****{name[-1]}@{domain}"
        
        else: 
            digits = [ch for ch in s if ch.isdigit()]
            local = "***-***-" + "".join(digits[-4:])
            country_len = len(digits) - 10
            
            if country_len == 0:
                return local
            else:
                return "+" + "*" * country_len + "-" + local
        