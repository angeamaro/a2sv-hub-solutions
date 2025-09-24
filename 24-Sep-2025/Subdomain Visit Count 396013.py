# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)
        
        for cp in cpdomains:
            count, domain = cp.split()
            count = int(count)
            parts = domain.split(".")
            
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                counter[subdomain] += count
        
        return [f"{cnt} {dom}" for dom, cnt in counter.items()]
        