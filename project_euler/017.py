first_digits = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
tens = ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')

def small_length(num):
    length = 0
    str_num = str(num)
    if num < 20:
        length = len(first_digits[num])
    elif num < 100:
        ones = len(first_digits[int(str_num[1])])
        tens_place = len(tens[int(str_num[0])])
        if str_num[1] == '0':
            length = tens_place
        else:
            length = ones + tens_place
    return length

def get_length(num):
    str_num = str(num)
    length = 0
    if num < 100:
        length = small_length(num)
    else:
        length = len(first_digits[int(str_num[0])]) + 7 #length of word 'hundred'
        if str_num[1:3] != '00':
            length += small_length(int(str_num[1:3])) + 3 #length of word 'and'
    return length

answer = 0
for num in range(1,1000):
    answer += get_length(num)
answer += 11 #for the letters to spell 'one thousand'
print(answer)