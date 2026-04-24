class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        #create two maps
        first = {}
        second = {}

        for i in range(0,len(s)):
            first[s[i]] = 1 + first.get(s[i], 0)
            second[t[i]] = 1 + second.get(t[i], 0)
        
        for i in first:
            if first[i] != second.get(i, 0):
                return False
        
            
        return True
       
        
        