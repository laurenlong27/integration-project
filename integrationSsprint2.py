#Lauren Long
#This code will act like an event planning simulation
print("Hello! Welcome to Pine Hill event planning!")
name1 = input("Hello player, please enter name: ")
print("Hello", name1+ ", welcome to Pine Hill, an event planning simulator!")
print("In this game you will be able to pick between food options, types of entertainment, and more while you try to plan the most perfect event!")    
print("The point of the game is to plan the best event with the money you are given without going over budget.")
#directions
print("Directions: Player will receive $20,000 to try and make an amazing event. Player will make descisons from choice options provided. Player will also be asked to input numbers. DO NOT GO OVER YOUR LIMIT.")
bankTotal = 20000
print("Bank:$",bankTotal, sep="")
print("$20000 has been added to your account. Your event planner's name is Sara, she will be your guide for planning the perfect event. Happy spending!")
print("Sara: Hi",name1 + "," , "my name is Sara and I will be helping you plan your event. I will be asking you questions and you will provide me with your answer.")
#assigning numbers to the type of event
birthdayParty = 1
weddingReception = 2
#input("pick and option: ")
print("You have two options for event types. Option 1: Birthday Party or Option 2: Wedding Reception")
venueChoice = int(input("Pick an option(1 or 2):" ))
#start birthday event code
if (venueChoice == 1):
    lateFeeAmount = 20000 % 10
    estimatedCost = 20000//50
    print("You picked Birthday Party!")
    birthdayVenueCost = 5000
    print("Your remaining total is now $", bankTotal - birthdayVenueCost)
    birthdayTotal = 15000
#start birthday entertainment code
    print("Next you will pick your type of entertainment. Option 1: Clown or Option 2: Balloon Animals.")
    clownEntertainment = 1
    balloonEntertainment = 2
    birthdayEntertainment = int(input("Pick an option (1): "))
    if (not birthdayEntertainment != 1):
        print("You picked Clown as your entertainment!")
        clownCost = 3000
        print("Your remaining total is now $", 15000 - clownCost)
        birthdayNewTotal = 12000
    elif (birthdayEntertainment == 2):
        print("You picked balloon animals as your entertainment!")
        balloonCost = 3000
        print("Your remaining total is now $", 15000 - balloonCost)
        birthdayNewTotal = 12000
    elif ((birthdayEntertainment != 1) and (birthdayEntertainment != 2 )):
        print("Invalid input. Restart program.")
    
#start birthday food for clown code
    print("Next you will pick what food to have. Option 1: Cupcakes, Option 2: Cake Pops")
    cupcakesFood = 1
    cakepopFood = 2
    birthdayFood = int(input("Pick an option (1 or 2): "))
    if (birthdayFood == 1):
            print("You picked cupcakes as your food!")
            cupcakeCost = 5
            numOfGuests = int(input("Enter number of guests: "))
            print("Your final total is now $", 12000 - (cupcakeCost * numOfGuests))
            birthdayFinalCostcc = 12000 - (cupcakeCost * numOfGuests)
            splitCost = int(input("How many people are you slitting the cost with?: "))
            endCost = (20000 - birthdayFinalCostcc) / splitCost
            print("Your total amount spent is $", endCost, ", and your leftover amout is $", (20000 - endCost))


            print("Wow good job! Do you think you passed the game? Let's find out!")
            print(".... Loading ..... Loading " * 4)
            if (20000 - endCost > 0):
                print("You passed the game!" + "Your score was ", 20000 - endCost)
            else:
                print("You failed! Better luck next time")
    elif (birthdayFood == 2):
            print("You picked cakepops as your food!")
            cakepopCost = 5
            numOfGuests = int(input("Enter number of guests: "))
            print("Your final total is now $", 12000 - (cakepopCost * numOfGuests))
            birthdayFinallCostcp = 12000 - (cakepopCost * numOfGuests)
            splitCost = int(input("How many people are you slitting the cost with?: "))
            endCost = (20000 - birthdayFinalCostcp) / splitCost
            print("Your total amount spent is $", endCost, ", and your leftover amout is $", (20000 - endCost))            
            print("Wow good job! Do you think you passed the game? Let's find out!")
            print(".... Loading ..... Loading " * 4)
            if (20000 - endCost > 0):
                print("You passed the game!" + "Your score was ", 20000 - endCost)
            else:
                print("You failed! Better luck next time")

    elif ((birthdayFood != 1) and (birthdayFood != 2 )):
        print("Invalid input. Restart Program.")
# wedding venue 
elif (venueChoice == 2):
    lateFeeAmount = 20000 % 10
    estimatedCost = 20000//50
    print("You picked Wedding Reception!")
    weddingVenueCost = 5000
    print("Your remaining total is now $", bankTotal - weddingVenueCost)
    weddingTotal = 15000
    print("Next you will pick your type of entertainment. Option 1: Band or Option 2: DJ")
    bandEntertainment = 1
    djEntertainment = 2
    weddingEntertainment = int(input("Pick an option(1 or 2): "))
# wedding entertainment
# band
    if (weddingEntertainment == 1):
        print("You picked Band as your entertainment!")
        bandCost = 3000
        print("Your remaining total is now $", 15000 - bandCost)
        weddingNewTotal = 12000
# dj 
    elif (weddingEntertainment == 2):
        print("You picked DJ as your entertainment!")
        djCost = 3000
        print("Your remaining total is now $", 15000 - djCost)
    elif  ((weddingEntertainment != 1) or (weddingEntertainment != 2 )):
        print("Invalid input. Restart Program.")
# wedding food
    print("Now you will pick what kind of food you want to serce at the wedding. Option 1: Chicken or Option 2: Fish")
    chickenFood = 1
    fishFood = 2
    weddingFood = int(input("Pick and option(1 or 2): "))
# chicken
    if (weddingFood == 1):
        print("You picked chicken as your food!")
        chickenCost = 5
        numOfGuests = int(input("Enter number of guests: "))
        print("Your final total is now $", 12000 - (chickenCost * numOfGuests))
        weddingFinalCostc = 12000 - (chickenCost * numOfGuests)
        splitCost = int(input("How many people are you slitting the cost with?: "))
        endCost = (20000 - weddingFinalCostc) / splitCost
        print("Your total amount spent is $", endCost, ", and your leftover amout is $", (20000 - endCost))       
        print("Wow good job! Do you think you passed the game? Let's find out!")
        print(".... Loading ..... Loading " * 4)
        if (20000 - endCost > 0):
            print("You passed the game!" + "Your score was ", 20000 - endCost)
        else:
            print("You failed! Better luck next time")

# fish
    elif (weddingFood == 2):
        print("You picked fish as your food!")
        fishCost = 5
        numOfGuests = int(input("Enter number of guests: "))
        print("Your final total is now $", 12000 - (fishCost * numOfGuests))
        weddingFinalCostf = 12000 - (fishCost * numOfGuests)
        splitCost = int(input("How many people are you slitting the cost with?: "))
        endCost = (20000 - weddingFinalCostf) / splitCost
        print("Your total amount spent is $", endCost, ", and your leftover amout is $", (20000 - endCost))         
        print("Wow good job! Do you think you passed the game? Let's find out!")
        print(".... Loading ..... Loading " * 4)
        if (20000 - endCost > 0):
            print("You passed the game!" + "Your score was ", 20000 - endCost)
        else:
            print("You failed! Better luck next time")
    elif ((weddingFood != 1) or (weddingFood != 2 )):
        print("Invalid input. Restart Program")
else:
    print("Invalid input. Restart program")
        




endStatement = ("Thank you for playing the event planning simulator! Come back soon!")
x = 0
for x in range (10):
    print(endStatement)





