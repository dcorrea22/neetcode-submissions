class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = set(nums)
        lst = []
        for i in s:
            lst.append({i: nums.count(i)})
        return list(key for d in (sorted(lst, key = lambda x: list(x.values())[0])[-k:])for key in d)
            