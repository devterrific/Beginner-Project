from random import shuffle

list = [" ", "O", " "]

def shufflelist(list):
    shuffle(list)
    return list




def guess():
    pick = ""
    while pick not in ["0", "1", "2"]:
        pick = input("PLease choose a number between 1,2 or 0")

    return int(pick)


def check_guess(mylist, pick):
    if list[pick] == "O":
        print("Congrat")
    else:
        print("Wrong number")
        print(mylist)

mylist = [" ","O", " "]

shufflelistt = shufflelist(list)

pickk = guess()

check_guess(shufflelistt, pickk)



