class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.nums = nums        
      
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse = True)[0:self.kth]

        return self.nums[-1]
        
