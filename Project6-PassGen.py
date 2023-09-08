import string
import secrets

def password_generator(length,upper,symbols):
    combination=string.ascii_lowercase+string.digits

    
    if upper:
        combination+=string.ascii_uppercase
    if symbols:
        combination+=string.punctuation
    print(combination)
    combination_length=len(combination)
    password=""

    for _ in range(length):
        password+=combination[secrets.randbelow(combination_length)]
    print(password)
if __name__=="__main__":
    password_generator(10,True,True)
