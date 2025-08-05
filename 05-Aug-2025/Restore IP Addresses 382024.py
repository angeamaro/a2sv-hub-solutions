# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        # Early return: an IP address can't have more than 12 digits (4 parts * 3 digits max)
        if len(s) > 12:
            return res

        def back(i: int, dots: int, ip: str):
            # If 4 segments are formed and the entire string is used, store the result
            if dots == 4 and i == len(s):
                res.append(ip[:-1])  # remove trailing dot
                return
            if dots > 4:
                return

            # Try segments of length 1 to 3
            for k in range(i, min(i + 3, len(s))):
                part = s[i:k + 1]
                # Skip if segment has leading zero or is greater than 255
                if int(part) < 256 and (i == k or s[i] != "0"):
                    back(k + 1, dots + 1, ip + part + ".")

        back(0, 0, "")
        return res
