#Understand
'''

    given s and t 
    if t and s are anagrams: both have teh same element types and each element type has a matching amount of numbers like a : 2 b :4 = a : 2 b : 4 then return true other wise return false

    needs two empty dictionaries that contain s and t and comapres them
    if s and t dont have the same length theryre obivously not anagrams
    we just need to know if a: 2 b:4 or b:4 and a:2 are equal in whatever order
    THEN RETURN IT
'''

#P
'''define two empty diciontarys
    loop for chracter in s or chracter in t
    take the first key so whatever letter like s and set it eq
    
'''

#I
#edge cases if its not equal

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_pocket = {}
        t_pocket = {}

        for char in s: 
            s_pocket[char] = s_pocket.get(char, 0) + 1
        for char in t: 
            t_pocket[char] = t_pocket.get(char, 0) + 1

        return s_pocket == t_pocket
               