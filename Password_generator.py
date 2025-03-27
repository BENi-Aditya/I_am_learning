import random

letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","m","m"]
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!','@','#','$','%','^','&','*','(',')']

num = int(input("How many numbers?\n"))
let = int(input("How many letters you want?\n"))
sym = int(input("How many symbols you want?\n"))

password = []

for i in range(num):
    x = random.randint(0, len(numbers)-1)
    password.append(str(numbers[x]))

for j in range(let):
    y = random.randint(0, len(letters)-1)
    password.append(letters[y])

for k in range(sym):
    z = random.randint(0, len(symbols)-1)
    password.append(symbols[z])

random.shuffle(password)

#final_password = str(password)
final_password = ''.join(password)
print(final_password)
