"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in intervals:
            for j in intervals:                
                if ((i.start <= j.start) and (i.end > j.start)) and i != j:
                    print("i: ", i.start)
                    print("j: ", j.start)
                    return False
        return True
        
        
