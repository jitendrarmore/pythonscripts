# import num2words
#
# number = 10
# print(num2words.num2words(10245))



below_ten = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
below_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
below_hundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

def numbersToWord(number):
    if number == 0:
        return "zero"

    return _convert_to_words(number)

def _convert_to_words(number):
     if number < 10:
         return below_ten[number]
     if number < 20:
         return below_twenty[number - 10]
     if number < 100:
         return below_hundred[number // 10] + (" " + _convert_to_words(number % 10) if number % 10 != 0 else "")
     if number < 1000:
         return _convert_to_words(number // 100) + " Hundred" + (" " + _convert_to_words(number % 100) if number % 100 != 0 else "")
     if number < 1000000:
         return _convert_to_words(number // 1000) + " Thousand" + (" " + _convert_to_words(number % 1000) if number % 1000 != 0 else "")
     if number < 1000000000:
         return _convert_to_words(number // 1000000) + " million" + (" " + _convert_to_words(number % 1000000) if number % 1000000 != 0 else "")
     return _convert_to_words(number // 1000000000) + " Billion" + (" " + _convert_to_words(number % 1000000000) if number % 1000000000 != 0 else "")

print(numbersToWord(1234567))