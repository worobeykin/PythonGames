#Power Ball Simulator App

import random

print("Welcome to the Power Ball Simulator App.")

#Get usrer choices
white_balls = int(input("\nHow many white balls whould you like to use(1-69): ").strip())

if white_balls < 5:
    white_balls = 5

red_balls = int(input("How many red balls whould you like to use(1-26): ").strip())

if red_balls < 1:
    red_balls = 1

# Determine the odds 
odds = 1
for i in range(5):
    odds *= white_balls - i
odds *= red_balls/120
print("You have a 1 in " + str(round(odds, 2)) + " chance of winning this lottery. ")

#Get user ticket amount
ticket_interval = int(input("How many ticket whould you like to purchase: ").strip())

winning_numbers = []
while len(winning_numbers) < 5:
    random_ball = random.randint(1, white_balls)
    if random_ball not in winning_numbers:
        winning_numbers.append(random_ball)
winning_numbers.sort()

random_red_ball = random.randint(1, red_balls)
winning_numbers.append(random_red_ball)


#Simulate the actual Power Ball drawing
print("\n\n-------Welcome to the Power-Ball-------")
print("\nTonights winning numbers are: " + ' '.join(str(value) for value in winning_numbers))
input("\nPress Enter to bay a ticket")

tickets_purchased = 0
active = True
tickets_sold = []

while winning_numbers not in tickets_sold and active == True:
    lottery_numbers = []
    while len(lottery_numbers) < 5:
        random_ball = random.randint(1, white_balls)
        if random_ball not in lottery_numbers:
            lottery_numbers.append(random_ball)
    lottery_numbers.sort()
    
    random_red_ball = random.randint(1, red_balls)
    lottery_numbers.append(random_red_ball)

    if lottery_numbers not in tickets_sold:
        tickets_purchased +=1
        tickets_sold.append(lottery_numbers)
        print(lottery_numbers)
    else:
        print("This ticket has been already bought!")


    if tickets_purchased % ticket_interval == 0:       
        print("\nThe total number of tickets bought: " + str(tickets_purchased))
        choice = input("\nWould you like to continue(y/n): ").strip().lower()
        if choice != 'y':
            active = False
        
if lottery_numbers == winning_numbers:
    print("\nYou won!!!")
    print("The winning number is: " + ' '.join(str(value) for value in lottery_numbers))
    print("You needed " + str(tickets_purchased) + " tickets")
else:
    print("\nYou did not win!!!")
    print("You bought " + str(tickets_purchased) + " tickets")
        
        

    




    
    
        
        
    
        



        






























        

    
