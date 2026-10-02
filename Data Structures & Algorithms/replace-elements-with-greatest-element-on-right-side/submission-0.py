class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i, num in enumerate(arr):
            greatest = 0
         
            for num2 in arr[i+1:]:
                if num2 > greatest:
                    greatest = num2
                
            arr[i] = greatest

        arr[-1] = -1
        return arr
             
        