# Line sweep (draw it out!)
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        res = []
        times = []
        balance = 0
        prevTime = None
        
        if len(schedule) == 0:
            return times
        
        for workTime in schedule:
            for time in workTime:
                times.append((time.start, 1))
                times.append((time.end, -1))
                
        times.sort() # automatically sorts by first number
        
        for time in times:
            if balance == 0 and prevTime != None and prevTime != time[0]:
                res.append(Interval(prevTime, time[0]))
            
            balance += time[1]
            prevTime = time[0]
            
        return res