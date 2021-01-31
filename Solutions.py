# leetcode

class Solution(object):
    #p1 
    def twoSum(self, nums, target):
        # brute force
        for i in range(len(nums)):
            for j in range(len(nums)):
                if ((nums[i] +  nums[j]) == target) & (i!=j):
                    return i,j
                else:
                    print('not found!')
                     
    #p2
    def maxProfit(self, prices):
        # brute force
        maxpB = 0
        for i in range(len(prices),-1,-1):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i] > maxpB:
                    maxpB = prices[j]-prices[i]
        
        # make quicker??
        minp = max(prices)+1
        maxp = 0
        for i in range(len(prices)):
            #print(prices[i],minp)
            if prices[i] < minp:
                minp = prices[i]
            if prices[i] - minp > maxp:
                maxp = prices[i] - minp
                  
        return maxp, maxpB

    #p3
    def containsDuplicate(self, nums):
        # brute force
        testB = False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    testB = True
                    break
        
        if len(nums) == 1:
            testB = False

        # faster?
        test = False
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                test = True
                break
                
        # even faster?
        seen = set()
        test2 = False
        for x in nums:
            if x not in seen:
                seen.add(x)
            else:
                test2 = True

        return test2,test,testB
    
    #p4
    def maxSubArray(self, nums):  
       # brute force
        test = min(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                sums = sum(nums[i:j])
                #print(nums[i:j],'total:',sums)
                if sums > test:
                    test = sums
                    
        # faster?


        return test
