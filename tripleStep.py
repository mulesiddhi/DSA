class Solution:
    def tripleStep(self,n:int):
        DP={}
        DP[0]=1
        DP[1]=1
        DP[2]=2
        for i in range(3,n+1):
            DP[i]=DP[i-1]+DP[i-2]+DP[i-3]
        return DP[n]
    
if __name__ == "__main__":
    s=Solution()
    print(s.tripleStep(4))
    print(s.tripleStep(5))
    print(s.tripleStep(6))
    