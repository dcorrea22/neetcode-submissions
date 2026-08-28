class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_window = [0] * 26
        l = 0
        r = 0
        biggest_str = 0                
        freq_window[ord(s[l]) - 65] += 1

        while r + 1 <= len(s) - 1:

            current_window = r - l + 1            

            if current_window - max(freq_window) <= k:
                r += 1
                freq_window[ord(s[r]) - 65] += 1                
                biggest_str = (max(biggest_str, current_window))                      

            else:
                freq_window[ord(s[l]) - 65] -= 1
                l += 1            

        current_window = r - l + 1

        if current_window - max(freq_window) <= k:
            biggest_str = (max(biggest_str, current_window))
            
        
        return biggest_str



            



        
        
        
            
        
