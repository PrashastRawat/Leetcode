class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            curs = intervals[i][0]
            cure = intervals[i][1]

            laste = res[-1][1]
            lasts = res[-1][0]
            if curs<=laste:
                if cure>laste:
                    res[-1][1]=cure
            else:
                res.append([curs,cure])
        return res