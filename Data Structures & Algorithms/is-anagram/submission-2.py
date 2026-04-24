class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check to see if the strings are the same length
        if len(s) != len(t):
            return False
        # now we will create maps that correlate to each string 
        x = {}
        y = {}
        for char in s:
            if char in x:
                x[char] += 1
            else:
                x[char] = 1
        for char in t:
            if char in y:
                y[char] += 1
            else:
                y[char] = 1
        if x == y:
            print('yes')
            return True
            
        else:
            print('no')
            return False
        