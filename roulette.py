import random

user_input=int(input("Faites vos jeux"))
print("Rien ne va plus")

def tourne_roulette():
    i=0
    while i<random.randint(5,15):
        print (random.randint(1,36))
        i+=1
    result = random.randint(1,36)
    print (result)
    return result

def result(bet,result):
    if bet == result:
        print("Youpie, vous avez gagné!")
    else:
        print("Perdu!")

result(user_input, tourne_roulette())


