#This program is written to encode plaintext to ciphertext through shifting the position of the alphabetical order
#This program is written by Ann

plaintext = input("Your message: ")
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
key = int(input("Letters shift: "))
letter_number = 0
total = ""
is_capital = True

def function(letter_number, key, is_capital, letter):
    if letter == " ":
        return(" ")
    ciphertext = ((letter_number + key) % 26) - 1
    if is_capital == True:
        return upper_case[ciphertext]
    else:
        return lower_case[ciphertext]
for x in range(len(plaintext)):
    letter = plaintext[0]
    for i in range(26):
        if  letter == upper_case[i]:
            letter_number = i + 1
            is_capital = True
        elif letter == lower_case[i]:
            letter_number = i + 1
            is_capital = False
    plaintext = plaintext[1:]
    total = total + function(letter_number, key, is_capital, letter)
print(total)
