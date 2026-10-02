class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        groups = {}
     
        for num in nums:
            groups[num] = groups.get(num, 0) + 1
        for numz in groups:
            numz = int(num)

        freqs = sorted(groups, key=lambda x: groups[x], reverse=True)
    
       
        


        return freqs[:k]

            
        