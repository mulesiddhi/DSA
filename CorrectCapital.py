"""
This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true

"""

class Solution:
    def correctCapital(self, s: str) -> bool:
        if s.isupper() or s.islower() or s[0].isupper() and s[1:].islower():
            return True
        else:
            return False

if __name__ == '__main__':
    s=Solution()
    print(s.correctCapital("USA")) # True
    print(s.correctCapital("Calvin")) # True
    print(s.correctCapital("compUter")) # False
    print(s.correctCapital("coding")) # True
    print(s.correctCapital("Coding")) # True
  