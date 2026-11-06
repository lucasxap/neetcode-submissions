class Solution:
    def trap(self, height: List[int]) -> int:

        #find the maximum height for water. then find the width
        #then for each collumn subtract the maximum height from the height of each column. for example 3 max and curret hiegh is 1 then only 2 waters tall can fit.
        #it needs a beging and end. two pointers for that. like a sliding window but different.
        #idk how it looks but basically u need a water checker and a total water.
        #cuz this is fixrd im just gonna make it until 

        total = 0
        #psuedo code. max height is min(left, right)
        #if curr > total then total == curr
        #some how implement this weird slicindg technique where you do like
        #water must be trapped between bars
        '''
        for example if indices 0 5 0 4 0 5
        then incidcies 1 and 5 and evertying inbetween those exludes indice 1 and 5
        so for indices 2 3 4 its like
        2: max - curr height 5
        3: max - curr height 1
        4: max - curr height  5
        based on this i think i might have to use two differnt types of a loop
        maybe a for each loop and when it ends it resests 1 after the right most 

        i think the left most block is temproarily static. make the right most block move until it hits something and then keep track of that height.
        i think if this is math term but in both bars they need some shared height for example, if left is 1 then right must have at least 1 
        if left is 5 then right must have at most 5
        so if height left is 2 then its at most 2 for the right side.
        if right side is 3 then its at most something.
        skip blocks that are right next to eachother because no water can fit inbetween and will save time
        skip blocks that have nothing like 0
        if you skip blocks that touch and blocks that are 0 i think based on how a cup works that might autoamtically determine the shape
        '''


        l, r = 0, len(height) -1
        lmax, rmax = height[l], height[r]
        total = 0 

        while l < r:

            if lmax < rmax:
                l +=1

                lmax = max(lmax, height[l])
                total += lmax - height[l]

            else:
                r -= 1
                rmax = max(rmax, height[r])
                total +=  rmax - height[r]
                
        
         
        return total
        