class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res=[]
        for i in range(len(strs)):
            if i!=0:
                res.append('#')
            for c in strs[i]:
                res.append(str(ord(c))+';')
            
        
        return ''.join(res)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res=[]
        strs=str.split('#')
        
        # print(strs)
        for s in strs:
            j=[]
            for k in s.split(';'):
                if k:
                    j.append(chr(int(k)))
           
            res.append(''.join(j))

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.decode(s.encode(["lint","code","love","you"]))==["lint","code","love","you"])
    print(s.decode(s.encode([""]))==[""])
    print(s.decode(s.encode(["we", "say", ":", "yes"]))==["we", "say", ":", "yes"])
    
