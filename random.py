import random

num = random.randint(1,100)
print(num)
life = 10
while True:
    m = int(input("enter number(1/100): "))
    if life > 0:
        if m == num:
            print("yes")
            break
        elif m < num:
            print("no, it's smaller")
            life -= 1
        elif m > num:
            print("no, it's biger")
            life -= 1
    else:
        print("you are lose please try agane")
        break