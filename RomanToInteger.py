# Analyzes a roman numeral in a string format and returns its integer translation
# Works for roman numerals up until 1000

class RomanToInteger(object):

    def __init__(self):
        self.roman_numeral = []
        self.value = 0

    def romanToInt(self, s):

        # Parses the input rn string
        for numeral in s:
            self.roman_numeral.append(numeral)


        # Handles exception cases (4, 9, 40, 90, etc.)
        def handle_exception_case(numeral, num_str, inc_value):

            self.roman_numeral.insert(self.roman_numeral.index(numeral), num_str)
            self.roman_numeral.pop(self.roman_numeral.index(numeral) + 1)
            self.roman_numeral.pop(self.roman_numeral.index(numeral))

            numeral = num_str

            self.value += inc_value

            return numeral


        for numeral in self.roman_numeral:

            # Exception cases (4, 9, 40, 90, etc.)
            # 4
            if self.roman_numeral[self.roman_numeral.index(numeral)] == 'I' and self.roman_numeral[self.roman_numeral.index(numeral) + 1] == 'V':
                numeral = handle_exception_case(numeral, 'IV', 4)
            
            # 9
            if self.roman_numeral[self.roman_numeral.index(numeral)] == 'I' and self.roman_numeral[self.roman_numeral.index(numeral) + 1] == 'X':
                numeral = handle_exception_case(numeral, 'IX', 9)

            # 40
            if self.roman_numeral[self.roman_numeral.index(numeral)] == 'X' and self.roman_numeral[self.roman_numeral.index(numeral) + 1] == 'L':
                numeral = handle_exception_case(numeral, 'XL', 40)

            # 90
            if self.roman_numeral[self.roman_numeral.index(numeral)] == 'X' and self.roman_numeral[self.roman_numeral.index(numeral) + 1] == 'C':
                numeral = handle_exception_case(numeral, 'XC', 90)

            # 400
            if self.roman_numeral[self.roman_numeral.index(numeral)] == 'C' and self.roman_numeral[self.roman_numeral.index(numeral) + 1] == 'D':
                numeral = handle_exception_case(numeral, 'CD', 400)

            # 900
            if self.roman_numeral[self.roman_numeral.index(numeral)] == 'C' and self.roman_numeral[self.roman_numeral.index(numeral) + 1] == 'M':
                numeral = handle_exception_case(numeral, 'CM', 900)
            

            # normal cases
            if numeral == 'I':
                self.value += 1
            if numeral == 'V':
                self.value += 5
            if numeral == 'X':
                self.value += 10
            if numeral == 'L':
                self.value += 50
            if numeral == 'C':
                self.value += 100
            if numeral == 'D':
                self.value += 500
            if numeral == 'M':
                self.value += 1000

        return self.value

rti = RomanToInteger()

num1 = "III"
num2 = "LVIII"
num3 = "MCMXCIV"

print(rti.romanToInt(num3))

