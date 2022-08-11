class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        s, e = 0, 0
        available = 0
        room = 0
        
        while s < len(start):
            if start[s] < end[e]:
                if available == 0:
                    room += 1
                    s += 1
                elif available > 0:
                    available -= 1
                    s += 1
            else:
                available += 1
                e += 1
        return room