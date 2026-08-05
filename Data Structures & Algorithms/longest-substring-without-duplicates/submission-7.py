class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        comparison = set()
        maximum = 0

        for k in range(len(s)):
            if s[k] not in comparison:
                comparison.add(s[k])                
                maximum = max(maximum, len(comparison))                
            else:
                while s[i] != s[k]:
                    comparison.discard(s[i])
                    i += 1
                i += 1
                            
                

                           
                
        return maximum
                

         
        