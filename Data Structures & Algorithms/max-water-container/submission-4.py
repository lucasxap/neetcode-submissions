#given height
#i need to constantly check a max 
#i cant sort it because it would ruin the width
#maybe i can check the area thats height and width and reject any height and width thats too low


class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        most = 0

        while left < right:
            

            width = right - left
            total = width * min(heights[right], heights[left])
            if total > most:
                print(left, right)
                most = total 
        

            if heights[left] > heights[right]:
                right -= 1

            else:
                left += 1
        return most
            




        