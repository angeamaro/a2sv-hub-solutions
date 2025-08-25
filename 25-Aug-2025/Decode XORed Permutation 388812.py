# Problem: Decode XORed Permutation - https://leetcode.com/problems/decode-xored-permutation/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        
        tot = 0
        for i in range(1, n + 1):
            tot ^= i

        odd = 0
        for i in range(1, len(encoded), 2):
            odd ^= encoded[i]
        
        first = tot ^ odd
        
        perm = [first]
        for code in encoded:
            perm.append(perm[-1] ^ code)
        
        return perm
        