from collections import deque

class HitCounter:

    def __init__(self):
        self.stamp = deque()
        self.count = 0
        

    def hit(self, timestamp: int) -> None:
        self.stamp.append(timestamp)
        self.count += 1

    def getHits(self, timestamp: int) -> int:
        while self.stamp:
            if timestamp - self.stamp[0] < 300:
                break
            self.stamp.popleft()
            self.count -= 1
            
        return self.count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)