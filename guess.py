import random
num = random.randint(1,20)
flag = False
for x in range (4):
    inp = int(input("guess the number between 1 and 20: "))
    if inp == num:
        print ("u have guessed the right number")
        flag = True
        break
    elif inp> num:
        print ("number is too high: ")

    else:
            print ("number is too low: ")

if flag == False:
    print ("sorry u ran out of guesses")
