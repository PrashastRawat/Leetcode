class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            curstart = intervals[i][0]
            curend = intervals[i][1]

            lstart = res[-1][0]
            lend = res[-1][1]
            if curstart<=lend:
                if curend>lend:
                    res[-1][1]=curend
            else:
                res.append([curstart, curend])
        return res