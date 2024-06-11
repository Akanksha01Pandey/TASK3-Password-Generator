import random
import string

lenght = int(input('Enter the lenght of password'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,lenght)
password = "".join(temp)
print(password)

