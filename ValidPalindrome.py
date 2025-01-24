# Analyzes a string and returns whether or not it is a palindrome

class Solution(object):

    def __init__(self):
        self.letters = []
        self.reversed_letters = []

    def reverseWords(self, s):
        # removes special characters, spaces, and converts uppercase characters to lower case
        s = s.replace(',', '')
        s = s.replace(';', '')
        s = s.replace(':', '')
        s = s.replace('!', '')
        s = s.replace('@', '')
        s = s.replace('#', '')
        s = s.replace('$', '')
        s = s.replace('%', '')
        s = s.replace('&', '')
        s = s.replace('*', '')
        s = s.replace(' ', '')
        s = s.lower()

        # populates the two letter arrays and reverses one of the arrays
        for letter in s:
            self.letters.append(letter)
            self.reversed_letters.append(letter)
        self.reversed_letters.reverse()

        # compares the two letter arrays
        if self.letters == self.reversed_letters:
            return "This is a palindrome"
        else:
            return "This is not a palindrome"


sol = Solution()

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

print(sol.reverseWords(s1))