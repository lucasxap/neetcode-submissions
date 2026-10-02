#given integer array nums and integer val
#remove all val in nums '

# CHANGE THE ARRYA NUMS usch that the first K  elements of nums contains the eoements which are not equal to val
#return number of items
#an elemnt thats not val is k

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
     

        for num in nums:
        
            if num != val:
                nums[k] = num
                k += 1
                
           
                
        return k
            


        