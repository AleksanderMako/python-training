class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda a: a[0])
        print(intervals)
        result = []
        for _,interval in enumerate(intervals):
            if len(result) < 1:
                result.append(interval)
            else:
                start = max(result[-1][0],interval[0])
                end = min(result[-1][1],interval[1])
                if end >= start:
                    result[-1][1]= max(interval[1],result[-1][1])
                else: result.append(interval)
        return result