'''
u

test cases 
[1, 2, 2, 3]


p

ok so basically just two sum but with while
i





'''

'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1

        while left < right:
            l = numbers[left]
            r = numbers[right]
            total = l + r
            if total == target:
                return [left+1, right +1]
            elif total < target:
                left += 1
            else:
                right -=1
        return []

'''





#use two poitners left and right, check for duplicates. the array will be presorted.



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1
    

        while left < right:
        
            sum = numbers[left] + numbers[right]

            if sum > target:
                right -= 1


            elif sum <target:
                left +=1

            else:
                return [left + 1, right + 1]
                
        return []
            