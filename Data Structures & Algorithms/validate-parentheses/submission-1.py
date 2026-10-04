#Understand given string of {} [] () 
#return true if everty open bracket is closed by the same type of close bracket
#open brackets are in the right oder
#every close bracket has a responding open bracket of the same type

#Plan: i think im gonna do someething like if the bracket infront of current bracket for example if its [ ( or {. then if its not followed, the its wrong
#edge case might be like frequency so like every thing needs to be an even number 2 so % 2 should be 0. i think you just do if s%2 = 0 then return false


#implement
class Solution:
    def isValid(self, s: str) -> bool:
        full = {"(":")","[":"]","{":"}" }
        closed = []
        opened = []
        group = []

        for char in s:
            if char in full:
                opened.append(char)
            elif char in full.values():
                if not opened or full[opened[-1]] != char:
                    return False
                opened.pop()
        return len(opened) == 0

                

        
