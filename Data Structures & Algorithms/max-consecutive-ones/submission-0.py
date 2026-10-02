#return max number of consecutive 1s

#less then 100k 
#
#check if number is a 1 
#count each one
#now we have total of one set
#does this new set of numbers has a greater max?
#temporary max and a new max

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxs = 0;
        maxtemp = 0;
        for i in range(len(nums)):
            j = i
            if nums[i] == 1:
                maxtemp += 1
                if maxtemp >= maxs :
                    maxs = maxtemp
            else:
                maxtemp = 0
        return maxs