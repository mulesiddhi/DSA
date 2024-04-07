"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tac t Coa
Output: Tru e (permutations : "tac o cat" , "atc o eta" , etc. ) 

"""
class Solution:
    def isPalindromePermutation(self,s):
        # def isPalindrome(s):
        #     lo=0
        #     hi=len(s)-1
        #     while lo<=hi:
        #         if s[lo]!=s[hi]:
        #             return False
        #         lo+=1
        #         hi-=1
        #     return True
        # def permutationSet(s):
        #     pass
        charSet=[0]*26
        for i in s:
            i=i.lower()
            if i.isalpha():
                charSet[ord(i)-ord('a')]+=1
        oddcount=0
        
        for i in (charSet):
            if i%2!=0:
                if oddcount==1:
                    return False
                oddcount=1
        return True
    
if __name__ == '__main__':
    s = input()
    obj = Solution()
    print(obj.isPalindromePermutation(s))
    # print(list(s))