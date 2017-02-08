# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
   string = x.to_s

   string == string.reverse
end
