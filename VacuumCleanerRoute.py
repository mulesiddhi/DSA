"""
Given a string representing the sequence of moves a robot vacuum makes,
 return whether or not it will return to its original position. 
The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.
Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true

"""
from collections import defaultdict

class Solution:
    def vacuumCleanerRoute(self, moves: str) -> bool:
        chars=defaultdict(int) #defaultvalue will be 0
        for i in moves:
            if i=='L':
                chars['L']+=1
            elif i=='R':
                chars['R']+=1
            elif i=='U':
                chars['U']+=1
            elif i=='D':
                chars['D']+=1
        return (chars['L']==chars['R']) and (chars['U']==chars['D'])

if __name__ == '__main__'  :
    s=Solution()
    print(s.vacuumCleanerRoute("LR")) # True
    print(s.vacuumCleanerRoute("URURD")) # False
    print(s.vacuumCleanerRoute("RUULLDRD")) # True
