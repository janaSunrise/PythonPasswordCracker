import itertools
import time
import string
import sys
with open('passphrases.txt','r') as f_open:
    data = f_open.read()

print('Thnaks You For Using It, If you Like it, Please contribute!')
time.sleep(3)
pas = str(input('What is your password > '))

def guess_password(real):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(1, 9):
      for guess in itertools.product(chars, repeat = password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return f'password is {guess}. found in {attempts} guesses.'
            print(guess, attempts)


print(guess_password(pas))