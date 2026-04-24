class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #first check to see if the strings are the same length
        if len(s) != len(t):
            return False
        #create two empty maps for each string
        #key is unique letter per string, value is amount of times letter occurs
        x = {}
        y = {}

        for i in range(len(s)):
            x[s[i]] = 1 + x.get(s[i], 0)
            y[t[i]] = 1 + y.get(t[i], 0)

        if (x == y):
            return True
        else:
            return False


        
        