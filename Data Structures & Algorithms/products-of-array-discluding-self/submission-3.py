class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        prefix = []
        postfix = []
        pre = 1
      

        for num in nums:
            output.append(pre)
            pre *= num
          
            
         
        pre = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= pre
            pre *= nums[i]
          
           
        
        
            
        
            
                    
           
        return output

        