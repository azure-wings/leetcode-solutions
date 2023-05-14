class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        size, i = len(intervals), 0

        while i < size - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals.insert(i, [intervals[i][0], max(intervals[i][1], intervals[i+1][1])])
                intervals.pop(i+1)
                intervals.pop(i+1)
                size -= 1
            else:
                i += 1

        return intervals