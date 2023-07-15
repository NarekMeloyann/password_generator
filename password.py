import string
import random

def generate_password(theLength):
    '''This functions is generate passwords'''
    letters = string.ascii_letters
    digits = string.digits
    totalChars = letters+digits
    finalResult = ""
    for i in range(theLength):
        finalResult+=random.choice(totalChars)

    return finalResult
def main():
    print("Enter password length")
    theLength = input()

    while True:
        try:
            theLength = int(theLength)
        except:
            print('Wrong passord length')
            continue

        thePassword = generate_password(theLength)
        print('The password is ' +thePassword)
        break

main()

