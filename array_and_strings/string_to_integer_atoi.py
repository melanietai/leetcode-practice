"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""
class Solution:
    def myAtoi1(self, s: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(s)
        
        INT_MAX = pow(2,31) - 1
        INT_MIN = -pow(2,31)
        
        # discard white spaces from beginning
        while index < n and s[index] == " ":
            index += 1
        
        # update sign
        if index < n and s[index] == "-":
            sign = -1
            index += 1
        elif index < n and s[index] == "+":
            index += 1
        
        # traverse next digits of s and stop if it is not a digit
        while index < n and s[index].isdigit():
            digit = int(s[index])
        
            # check overflow and underflow conditions
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = 10 * result + digit
            index += 1
            
        return sign * result
    
# using OOP - Deterministic Finite Automation (DFA)
# State machine reads input and changes the state accordingly
# a finite state machine either accepts or rejects a sequence of inputs by running through a sequence of states is called DFA
# there is only one path for specific input from the current state to the next state
# DFAs are useful in recognize patterns in data

class Solution:
    def myAtoi2(self, s: str) -> int:
        q = StateMachine()
        for ch in s:
            q.change_state(ch)
            if q.current_state == "qd":
                break
        return q.get_result()
        
        
class StateMachine:
    def __init__(self):
        self.INT_MAX = pow(2, 31) - 1
        self.INT_MIN = -pow(2, 31)
            
        self.current_state = "q0"
        self.result = 0
        self.sign = 1
    
    def to_state_q1(self, ch):
        self.current_state = "q1"
        if ch == "-":
            self.sign = -1
    
    def to_state_q2(self, int):
        self.current_state = "q2"
        self.append_digit(int)
    
    def to_state_qd(self):
        self.current_state = "qd"
    
    def append_digit(self, int):
        if ((self.result > self.INT_MAX // 10) or (self.result == self.INT_MAX // 10 and int > self.INT_MAX % 10)):
            if self.sign == 1:
                self.result = self.INT_MAX
            else:
                self.result = self.INT_MIN
                self.sign = 1
                
            self.to_state_qd()
        else:
            self.result = self.result * 10 + int
    
    def change_state(self, ch):
        if self.current_state == "q0":
            if ch == " ":
                return
            elif ch == "-" or ch == "+":
                self.to_state_q1(ch)
            elif ch.isdigit():
                self.to_state_q2(int(ch))
            else:
                self.to_state_qd()
        elif self.current_state == "q1" or self.current_state == "q2":
                if ch.isdigit():
                    self.to_state_q2(int(ch))
                else:
                    self.to_state_qd()
        
    def get_result(self):
        return self.sign * self.result