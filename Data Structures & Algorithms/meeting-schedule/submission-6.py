"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        list_sorted = sorted(intervals, key=lambda i: i.start)
        for i in range(1, len(list_sorted)):
            if list_sorted[i].start < list_sorted[i-1].end:
                return False
        return True

        
        
        
        
