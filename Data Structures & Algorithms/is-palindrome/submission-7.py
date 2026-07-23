class Solution:
    def isPalindrome(self, s: str) -> bool:
        collapsed = ''.join(e for e in s if e.isalnum())
        mid = len(collapsed) // 2         

        if len(collapsed) % 2 == 1:
            if collapsed[:mid].lower() == collapsed[mid + 1:][::-1].lower():
                return True
            else:
                return False
        else:
            if collapsed[:mid].lower() == collapsed[mid:][::-1].lower():
                return True
            else:
                return False
