class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
 

       
        for i ,num1 in enumerate(nums, start = 0):
      
           
            

            for j, num2 in enumerate(nums, start = 0):
                if num1 + num2 == target and i != j:
                    return[i, j]
               
                    
          

        












        
















        



