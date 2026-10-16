import math
class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        #u palindrome is a string thats same backwards anf forwards.
        #use lower cuz its case insnetitive
        #avoids non alphanumeric
        #must use the two pointer aproach
        #plan 
        #one pointer left one pointer right 
        #ignore spaces because a space is non alphanumeric

        #use is alphanumeric and then append all of them into a list
        # check if left = right 
        #weew i think the condition for when it stops is when the pointers are like equal because to the middle or half. cuz if its like
        #weeieew if we choose 4 as the middle then its fine because i should = i anywasy and return condition would still be true and return false if it wasnt so like math.ceil(len(s)/2) or just left and right i guesse
        st = []
        for char in s:
            if char.isalnum():
                st.append(char.lower())
        print(st)
        left = 0 
        right = len(st)-1
        print(len(st))

        while left < right:
            print(st[left], left, st[right], right)
            if st[left] != st[right]:
                return False 
            left += 1
            right -= 1
        return True

        