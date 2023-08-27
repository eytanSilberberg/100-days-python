import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters=int(input("How many letters would you like to have in your password? "))
num_nums=int(input("how many numbers would you like to have in your password? "))
num_symbols=int(input("How many symbols would you like to have in your password? "))

# One way
# password=''
# for i in range(0,num_letters):
#     password=password+letters[random.randint(0,len(letters)-1)]

# for i in range(0,num_nums):
#     rand_num=numbers[random.randint(0,len(numbers)-1)]
#     rand_str_idx=random.randint(0,len(password))
#     password=password[:rand_str_idx]+rand_num+password[rand_str_idx:]

# for i in range(0,num_nums):
#     rand_sym=symbols[random.randint(0,len(symbols)-1)]
#     rand_str_idx=random.randint(0,len(password))
#     password=password[:rand_str_idx]+rand_sym+password[rand_str_idx:]


# Second way
password=[]

for i in range(0,num_letters):
    password+=random.choice(letters)
for i in range(0,num_nums):
    password+=random.choice(numbers)
for i in range(0,num_symbols):
    password+=random.choice(symbols)
random.shuffle(password)
password=''.join(password)
print(password)
