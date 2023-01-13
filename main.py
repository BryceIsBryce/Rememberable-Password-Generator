import random
import json

def password_generator():
    file = open("nouns.json")
    nouns = json.load(file)
    file.close()
    numbers = random.randint(1000,9999)
    password = random.choice(nouns) + "_" + str(numbers)
    return password

def run():
    while True:
        try:
           num = int(input("Amount of Generated Passwords: \n"))
           if num > 0:
               break
           else:
               print("\nInput needs to be a positive number\n")
        except ValueError:
           print("\nInput needs to be a positive number\n")
    place = 0
    print()
    while place < num:
        place += 1
        print(password_generator())
    print()

run()
