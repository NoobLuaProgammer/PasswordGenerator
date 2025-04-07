import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!£$%^&*()-=+_][}{#'~@;:/?.,><\""
length = int(input("How long do you want the password to be?: "))
result = ''.join(random.choice(characters) for i in range(length))
print(result)
