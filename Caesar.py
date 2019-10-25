#This program is written to encode plaintext to ciphertext through shifting the position of the alphabetical order
#This program is written by Ann

plaintext = input("Your message: ")
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
key = int(input("Letters shift: "))
letter_number = 0
total = ""
is_capital = 1

def function(letter_number, key, is_capital, letter):
    ciphertext = ((letter_number + key) % 26) - 1
    if is_capital == 1:
        return upper_case[ciphertext]
    elif is_capital == 0:
        return lower_case[ciphertext]
    else:
        return(letter)
for x in range(len(plaintext)):
    letter = plaintext[0]
    for i in range(26):
        if  letter == upper_case[i]:
            letter_number = i + 1
            is_capital = 1
        elif letter == lower_case[i]:
            letter_number = i + 1
            is_capital = 0
        else:
            is_capital = 2
    plaintext = plaintext[1:]
    total = total + function(letter_number, key, is_capital, letter)
print(total)
