import random
import string

length = int(input("Length: "))
prefix_flag = input("Prefix: ")

def generate_flag():
    flag = prefix_flag + "{"
    for i in range(0,length):
        flag += str(random.choice(f"{string.ascii_letters}{string.digits}"))   
    flag += "}"
    print(flag)

generate_flag()






