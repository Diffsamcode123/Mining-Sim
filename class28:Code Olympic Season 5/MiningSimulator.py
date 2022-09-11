
from random import randint

creadits="""
created by Samik
"""
money=40

achievements=[]

bag=[]

woodenPicaxeQuality=0

location = {
    "1 - Desert":{" Earning Limit":47,"Success Percetage":70},
    "2 - Cave":{"Earning Limit":98,"Success Percentage":85},
}

def gap():
  print()


def line2():
  print("************************************************")
  
def line3():
  print("================================================")

def line1():
  print("------------------------------------------------")

def line4():
  print("''''''''''''''''''''''''''''''''''''''''''''''''")

def line5():
  print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

def line6():
  print("????????????????????????????????????????????????")

def line7():
  print("#################################################")

def checkGameOver():
    if money>1500:
        line2()
        print("You now have more then $200. Now you have the option finishing the game enter 1 or continue with the game enter 2: ")
        fch=input("Enter you option: ")

        if fch=="1":
            print("Going home.....")
            print(f"You told you Mom I made {money}")
            print("You Finished the game!!!!!!!!!!!!!!!!!!!!!!!!!!")

        elif fch=="2":
            print("Enjoy playing more!")

        else:
            print("Invaild")




def mining():
    global woodenPicaxeQuality
    global money
  
    if not("Wooden Picaxe" in bag or "Stone Picaxe" in bag or "Iron Picaxe" in bag or "Copper Picaxe" in bag):
        gap()
        line6()
        print("Where is you picaxe??? Buy a picaxe")
        line6()
        return

    if woodenPicaxeQuality=="0":
        gap()
        line7()
        print("Your picaxe is broken. Buy a picaxe")
        line7()
        return
    
    gap()
    print(location)
    line2()
    ch=input("Enter the location you want to got to: ")

    if ch=="1":
        gap()
        print("Going To Desert.....")
        print("Mining.....")
        woodenPicaxeQuality=woodenPicaxeQuality-1
        x=randint(1,100)
        if x<70:
            cost=randint(1,47)
            money=money+cost
            gap()
            line5()
            print(f"You made ${cost}")
            line5()
            gap()
        checkGameOver()

    elif ch=="2":
        print("Going to Cave.....")
        print("Mining.....")
        woodenPicaxeQuality=woodenPicaxeQuality-1
        x=randint(1,100)
        if x<85:
            cost=randint(1,98)
            money=money+cost
            gap()
            line5()
            print(f"You made ${cost}")
            line5()
            gap()
            checkGameOver()
        
        else:
            gap()
            print("made $0")




def shop():
    global money
    global woodenPicaxeQuality
    while True:
        gap()
        print(f"Money remaining:${money}")
        line4()
        print("Picaxes...")
        print("11 - Wooden Picaxe - Can use 10 Times - $25")
        print("12 - Stone Picaxe - Can use 20 Times - $43")
        print("13 - Iron Picaxe - Can use 40 Times - $79")
        print("14 - Copper Picaxe - Can use 80 Times - $149")
        line4()
        print("Mining Backpack...")
        print("21 - 5 Capacity Backpack - $15")
        print("22 - 10 Capacity Backpack - $40")
        print("23 - 20 Capacity Backpack - $80")
        line4()
        buy=input("Enter you want by puting the name of the thing or enter bye if you want to leave the shop: ")
        if buy=="11":
            gap()
            print("Purchased ... Wooden Picaxe")
            money=money-25
            bag.append("Wooden Picaxe")
            woodenPicaxeQuality=woodenPicaxeQuality+10
            achievements.append("Purchased ... Wooden Picaxe")


        elif buy=="21":
            gap()
            print("Purchased ... 5 Capacity Backpack")
            money=money-15
            bag.append("5 Capacity Bag")
            achievements.append("Purchased ... 5 Capacity Backpack")
        
        elif buy=="12":
            gap()
            print("Purchased ... Stone Picaxe")
            money=money-43
            bag.append("Stone Picaxe")
            achievements.append("Purchased ... Stone Picaxe")

        elif buy=="22":
            gap()
            print("Purchased ... 10 Capacity Backpack")
            money=money-40
            bag.append("10 Capacity Backpack")
            achievements.append("Purchased ... 10 Capacity Backpack")

        elif buy=="13":
            gap()
            print("Purchased ... Iron Picaxe")
            money=money-79
            bag.append("Iron Picaxe")
            achievements.append("Purchased ... Iron Picaxe")

        elif buy=="23":
            gap()
            print("Purchased ... 20 Capacity Backpack")
            money=money-80
            bag.append("20 Capacity Backpack")
            achievements.append("Purchased ... 20 Capacity Backpack")

        elif buy=="14":
            gap()
            print("Purchased ... Copper Picaxe") 
            money=money-149
            bag.append("Copper Picaxe")
            achievements.append("Purchased ... Copper Picaxe")

        elif buy=="bye":
            gap()
            print("Thanks for shopping")
            break
        
        else:
            print("Invalid input")


line1()
print("Welcome To Mining Simulator")
line1()

print("So this a little story that has happened to you so far:")
print("Your mom said go make some money and i will give you a hundred dollars.")
print("You spent 60 dollars on food and water now you are left with 40 dollars.")
print("Now the cheapest job is the mining job(of cousre not in real life).")
print("Now the story is over but so have to get gear you go to the shop and get a picaxe and mining backpack.")
line1()

while True:
    gap()
    line3()
    print("MAIN MENU")
    line3()
    print("1 - Shop")
    print("2 - Mining")
    print("3 - Check Bag")
    print("4 - Go To Bank")
    print("5 - See Achievements")
    print("6 - Check Picaxe")
    print("7 - Exit Game")
    line3()

    ch=input("Enter your choice: ")

    if ch=="1":
        shop()
    
    elif ch=="2":
        mining()

    elif ch=="3":
        print(bag)

    elif ch=="4":
        print("Going to the bank.....")
        gap()
        line5()
        print(f"${money}")
        line5()

    elif ch=="5":
      print(achievements)

    elif ch=="6":
        gap()
        
        print(f"You can use you Picaxe {woodenPicaxeQuality} Times...")
    
    elif ch=="7":
        print(creadits)
        break

    else:
        print("Invaild")
