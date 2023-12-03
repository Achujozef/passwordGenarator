import random
import string



def genarate_password(length, uppercase, lowercase , numbers , symbols):
    char =''
    if uppercase:
        char += string.ascii_uppercase
    if lowercase:
        char += string.ascii_lowercase
    if numbers:
        char += string.digits
    if symbols:
        char += string.punctuation
    if not char:
        print("No char Found")
    password = ''.join(random.choice(char)for ln in range(length))
    return password


length = int(input("Enter The Length of Password"))
uppercase=input("Include Uppercase 'y' for Yes and 'n' for No : ").lower()=='y'
lowercase=input("Include lowercase 'y' for Yes and 'n' for No : ").lower()=='y'
numbers=input("Include numbers 'y' for Yes and 'n' for No : ").lower()=='y'
symbols=input("Include symbols 'y' for Yes and 'n' for No : ").lower()=='y'


password=genarate_password(length, uppercase, lowercase , numbers , symbols)

print(password)