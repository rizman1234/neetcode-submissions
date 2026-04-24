import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #only leave alphanumeric values
        new = re.sub('[\W_]+',"",s).lower()
        print(new)

       
        pointer_one = 0
        pointer_two = len(new) - 1

        for i in range(len(new)):
            if new[pointer_one] == new[pointer_two]:
                pointer_one = pointer_one + 1
                pointer_two = pointer_two - 1
                continue
            else:
                return False

        return True

    