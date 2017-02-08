class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #if x is positive
        if x >=0:
            reverse = int(str(x)[::-1])
            #if reverse is valid 32bit int return reverse
            if (reverse < 2147483647):
                return reverse
            else:
                return 0
        #if x is negative
        else:
            #if reverse is valid 32bit int return reverse
            reverse = int("-"+str(x)[:0:-1])
            if (reverse > -2147483648):
                return reverse
            else:
                return 0
