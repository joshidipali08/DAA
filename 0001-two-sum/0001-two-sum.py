class Solution:
    def twoSum(self,num,target):# self call current obj
        for i in range (len(num)):
            for j in range (i+1,len(num)):
                if num[i]+num[j] == target:
                    return (i,j)

s=Solution()
print(s.twoSum)

        