class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for element in set(s):
            dict_s[element] = s.count(element)
        for element in set(t):
            dict_t[element] = t.count(element)

        if dict_s == dict_t:
            return True
        return False
        