"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale , pi e - > true
pales , pal e - > true
pale , bal e - > true
pale , bak e - > false
"""

class Solution:
    def oneEditAway(self,s1,s2):
        if abs(len(s1)-len(s2))>1:
            return False
        if len(s1)==len(s2):
            diff=0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    diff+=1
                if diff>1:
                    return False
            return True
        else:
            edit=0
            if len(s1)>len(s2):
                i=0
                j=0
                while i<len(s1) and j<len(s2):
                    if s1[i]!=s2[j]:
                        edit+=1
                        i+=1
                    else:
                        i+=1
                        j+=1
                    if edit>1:
                        return False
                return True
            else:
                i=0
                j=0
                while i<len(s1) and j<len(s2):
                    if s1[i]!=s2[j]:
                        edit+=1
                        j+=1
                    else:
                        i+=1
                        j+=1
                    if edit>1:
                        return False
            return True
            

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    obj = Solution()
    print(obj.oneEditAway(s1,s2))