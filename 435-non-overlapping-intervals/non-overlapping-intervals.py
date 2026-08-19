class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        count = 0
        last_end = intervals[0][1]
        for i in range(1,len(intervals)):
            curs = intervals[i][0]
            cure = intervals[i][-1]

            if curs<last_end:
                count+=1
            else:
                last_end = cure
        return count