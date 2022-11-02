import random,string

def name(passlength):
    password=""
    for i in range(passlength):
        letter=""
        beeboo=random.randint(1,4)
        if beeboo==1:
            letter=str(random.choice(string.ascii_uppercase))
        if beeboo==2:
            letter=str(random.choice(string.ascii_lowercase))
        if beeboo==3:
            letter=str(random.choice(string.digits))
        if beeboo==4:
            beeboo2=random.randint(1,8)
            if beeboo2==3:
                letter=str("*")
        password=password+letter
    print(password)

amount = int(input("amount: "))
length = int(input("passlen: "))
for i in range(amount):
    name(length)
yes = input()