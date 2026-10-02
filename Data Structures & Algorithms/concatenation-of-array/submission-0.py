'''
U: given integer array numbers of length n
create an array ans of length 2n
an element at an index i for both ans and nums must be the same 
the element in ans[i+n] must be the same as nums[i]
return ans 

: define ans and make it twice the size as n. you can do this by 
ans  1 2 3 4 1 2 3 4
nums 1 2 3 4 

based on the math i dont need an conditionals i just need to add the list in front of itsself

'''




class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        return nums + nums
        
      

        