# Reverses the words in a string sentence

class Solution(object):
    def reverseWords(self, s):
        
        words = s.split()
        words.reverse()
        reversed_s = " ".join(words)

        return reversed_s


sol = Solution()

s1 = "the sky is blue"
s2 = "hello world"
s3 = "a         good                 example       "

print(sol.reverseWords(s3))