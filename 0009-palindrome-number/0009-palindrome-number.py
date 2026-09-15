class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        result=0
        original=x

        if(x<0):
            return False
        
        while x>0:
            last_digit=x%10
            result= (result*10)+last_digit
            x=x//10

        return original==result

                


        