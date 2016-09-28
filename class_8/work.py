#exercise 1
def excersize_1():
    suffixes = ['J','K','L','M','N','Ou','P','Qu']
    for x in suffixes:
        print(x + 'ack')

#exercise 2
def character_count(my_string, a):
    answer = 0
    for letter in my_string:
        if letter == a:
            answer += 1
    return answer

#exercise 4
def word_value(word):
    total = 0
    for letter in word:
        total += ord(letter) - 96
    return float(total)

def receipt(my_list):
    max_length = 0
    for word in my_list:
        if len(word) > max_length:
            max_length = len(word)
    grand_total = 0
    for word in my_list:
        print('{:{align}{width}}'.format(word, align='<', width=str(max_length+4))+'{:{align}{width}}'.format('$'+ str(word_value(word))+'0', align='>', width='5'))
        grand_total += word_value(word)
    print('--------------------------')
    print('{:{align}{width}}'.format('Total', align='<', width=str(max_length+4))+'{:{align}{width}}'.format('$'+ str(grand_total)+'0', align='>', width='5'))

item_list = ['bananas', 'rice', 'paprika', 'potato chips', 'stuff', 'other stuff']

receipt(item_list)

#exercise 5

#the first function only returns true or false of the first letter, then stops

#the second function checks the letter 'c' instead of the string stored in c, and it returns a string 'true' or 'false'
#instead of the True or False operators

#the third function only returns whether the last character is lowercase, because the flag variable keeps getting reassigned

#the fourth function works for the intended purpose - if any character is found to be True, flag will be assigned True, 
#and by the or statement will always be True thereafter

#the fifth function doesn't work because any character found to be not lowercase will return False and end the function

#exercise 6
def rotate_word(my_word, rotate):
    final_string = ''
    for char in my_word:
        if char.isalpha():
            new_letter = chr((ord(char.lower()) - 97 + rotate) % 26 + 97)
            final_string += new_letter
        else:
            final_string += char
    return final_string