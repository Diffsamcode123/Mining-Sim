
from random import randint

creadits=2

money=40

achievements=[]

bag=[]

location = {
    "1 - Desert":{"limit":47,"percetage":20},
    "2 - Cave":{"limit":98,"percentage":10},
}

def checkGameOver():
    if money>200:
        print("You now have more then $200. Now you have the option finishing the game enter 1 or continue with the game enter 2: ")
        fch=input("Enter you option: ")

        if fch=="1":
            print("Going home.....")
            print(f"You told you Mom i made {money}")
            print("You Finisheed the game!!!!!!!!!!!!!!!!!!!!!!!!!!")

        elif fch=="2":
            print("Enjoy playing more!")

        else:
            print("Invaild")

def sell():
    pass

def mining():
    global money
    print(location)
    ch=input("Enter the location you want to got to: ")

    if ch=="1":
        print("Going To Desert.....")
        print("Mining.....")
        x=randint(1,100)
        if x<70:
            cost=randint(1,47)
            money=money+cost
            print(f"You made ${cost}")
        checkGameOver()

    elif ch=="2":
        print("Going to Cave.....")
        print("Mining.....")
        x=randint(1,100)
        if x<85:
            cost=randint(1,98)
            money=money+cost
            print(f"You made ${cost}")
            checkGameOver()
        
        else:
            print("made $0")


def shop():
    global money
    while True:
        print(f"Money remaining:${money}")
        print("-----------------Picaxes---------------------")
        print("11 - Wooden Picaxe - Can use 10 Times - $25")
        print("12 - Stone Picaxe - Can use 20 Times - $43")
        print("13 - Iron Picaxe - Can use 40 Times - $79")
        print("14 - Copper Picaxe - Can use 80 Times - $149")
        print("---------------Mining Backpack---------------")
        print("21 - 5 Capacity Backpack - $15")
        print("22 - 10 Capacity Backpack - $40")
        print("23 - 20 Capacity Backpack - $80")
        buy=input("Enter want you want by puting the name of the thing or enter bye if you want to leave the shop: ")
        if buy=="11":
            print("Purchased ... Wooden Picaxe")
            money=money-25
            bag.append("Wooden Picaxe")
            achievements.append("Purchased ... Wooden Picaxe")


        elif buy=="21":
            print("Purchased ... 5 Capacity Backpack")
            money=money-15
            bag.append("5 Capacity Bag")
            achievements.append("Purchased ... 5 Capacity Backpack")
        
        elif buy=="12":
            print("Purchased ... Stone Picaxe")
            money=money-43
            bag.append("Stone Picaxe")
            achievements.append("Purchased ... Stone Picaxe")

        elif buy=="22":
            print("Purchased ... 10 Capacity Backpack")
            money=money-40
            bag.append("10 Capacity Backpack")
            achievements.append("Purchased ... 10 Capacity Backpack")

        elif buy=="13":
            print("Purchased ... Iron Picaxe")
            money=money-79
            bag.append("Iron Picaxe")
            achievements.append("Purchased ... Iron Picaxe")

        elif buy=="23":
            print("Purchased ... 20 Capacity Backpack")
            money=money-80
            bag.append("20 Capacity Backpack")
            achievements.append("Purchased ... 20 Capacity Backpack")

        elif buy=="14":
            print("Purchased ... Copper Picaxe") 
            money=money-149
            bag.append("Copper Picaxe")
            achievements.append("Purchased ... Copper Picaxe")

        elif buy=="bye":
            print("Thanks for shopping")
            break
        
        else:
            print("Invalid input")

print("Welcome To Mining Simulator")

print("So this a little story that has happened to you so far:")
print("Your mom said go make some money and i will give you a hundred dollars.")
print("You spent 60 dollars on food and water now you are left with 40 dollars.")
print("Now the cheapest job is the mining job(of cousre not in real life).")
print("Now the story is over but so have to get gear you go to the shop and get a picaxe and mining backpack.")

while True:
    print("1 - Shop")
    print("2 - Mining")
    print("3 - Sell")
    print("4 - Check Bag")
    print("5 - Go To Bank")
    print("6 - Exit Game")

    ch=input("Enter your choice: ")

    if ch=="1":
        shop()
    
    elif ch=="2":
        mining()

    elif ch=="3":
        sell()

    elif ch=="4":
        print(bag)

    elif ch=="5":
        print("Going to the bank.....")
        print(f"${money}")

    elif ch=="6":
        print(creadits)
        break

    else:
        print("Invaild")
