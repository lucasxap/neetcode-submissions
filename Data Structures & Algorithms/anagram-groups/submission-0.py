#return a list of sublist composing of groups of anagrams

#lower cases only test cases not really


#plan
#make a has of a sorted word and then sort ever word in a loop and assign them as keys 
#then return those as list 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for str in strs:

            key = "".join(sorted(str))
            if key not in groups:
                groups[key] = []
            groups[key].append(str)



        return list(groups.values())
