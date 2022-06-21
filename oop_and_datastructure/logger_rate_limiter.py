"""
Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.
"""
class Logger:

    def __init__(self):
        self.log = {} # store message and timestamp info

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # dict: {message: timestamp} - update each time same message appears; new entry if new message
        resp = True
        
        if self.log.get(message):
            if timestamp < self.log[message]:
                resp = False
            else:
                self.log[message] = timestamp + 10
        else:
            self.log[message] = timestamp + 10
        return resp


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

from collections import deque

class Logger:

    def __init__(self):
        self.set = set()
        self.queue = deque()
    
    def shouldPrintMessage(self, timestamp, message):

        while self.queue:
            msg, ts = self.queue[0]
            if timestamp - ts >= 10:
                self.set.remove(msg)
                self.queue.popleft()
            else:
                break
        
        # if old message has expired, can print new message
        # if old message hasn't expired, cannot print new message
        if message not in self.set:
            self.set.add(message)
            self.queue.append((message, timestamp))
            return True
        else:
            return False