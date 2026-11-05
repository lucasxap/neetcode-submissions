#u, given nums array. return triplets taht equal 0. i k and k
#im guessing like brute force or maybe recursion??
#well pointers use while loops
#maybe a binary search with 3 pointers somehow
#for loop with while loop two poitner inside left and right.



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue 
            
            j, k = i + 1, len(nums)-1 
            while j < k:
                three_sum = a + nums[j] + nums[k]
                if three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    final.append([a, nums[j], nums[k]])
                    k -= 1
                    j += 1

                    while j < k and nums[j] == nums[j-1]:
                            j += 1

                    while j < k and nums[k] == nums[k+1]:
                            k -=1
        return final
        