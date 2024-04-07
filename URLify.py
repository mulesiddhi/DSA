"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr 3ohn Smit h 13
Output: "Mr%203ohn%20Smith" 
"""
class Solution:
    def URLify(self,s,n):
        s=list(s)
        for i in range(n):
            if s[i].isalpha()==False:
                s[i]='%20'
        return ''.join(s)

if __name__ == '__main__':
    s = input()
    n= int(input())
    obj = Solution()
    print(obj.URLify(s,n))
    # print(list(s))
