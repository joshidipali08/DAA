class Solution:
    def twoSum(self,num,target):# self call current obj
        for i in range (len(num)):
            for j in range (i+1,len(num)):
                if num[i]+num[j] == target:
                    return (i,j)

s=Solution()
print(s.twoSum)

# outer loop runs n times , inner loop can also run up to n times. tc = O(n × n) = O(n²)
#variables (i, j) are used.sc =O(1)