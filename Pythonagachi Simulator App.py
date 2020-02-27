#Pythonagachi Simulator App
import random

#Class block
class Creature():
    """Create a simple Tomogachi clone."""
    
    def __init__(self, name):
        """Initialize attributes"""
        self.name = name.title()
        
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0      
        self.dirtiness = 0
        
        self.food = 2
        self.is_sleeping = False
        self.alive = True

    def eat(self):
        """The method describing food"""
        if self.food > 0:
            self.food -= 1
            self.hunger -= random.randint(1, 4)
            print("\nmmm...The creature ate a great meal!")
        else:
            print("\nThe creature has no food")
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        """The method describing play"""
        creature_riddle_value = random.randint(0, 2)
        print("\nThe creature wants to play a game!")
        print("The creature is thinking of a number 0, 1, or 2")
        user_riddle_value = int(input("Enter your value: "))
        if creature_riddle_value == user_riddle_value:
            print("It is true!!! Ohhhlala")
            self.boredom -= 3
        else:
            print("Oh no you are wrong!!! It is terrible")
            self.boredom -= 1
        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        """The method describing sleep"""
        self.is_sleeping = True
        self.boredom -= 2
        self.tiredness -= 3
        print("\nThe creature is sleeping now...")
        if self.tiredness < 0:
            self.tiredness = 0
        if self.boredom < 0:
            self.boredom = 0

    def awake(self):
        """The method describing awake"""
        chance_awake = random.randint(0, 2)
        if chance_awake == 0:
            print("\nThe creature just woke up")
            self.is_sleeping = False
            self.boredom = 0
        else:
            print("\nThe creature just won’t wake up")
            self.sleep() 

    def clean(self):
        """The method describing dirtiness"""
        self.dirtiness = 0
        print("\nThe creature took a bath")
        
    def forage(self):
        """The method describing forage"""
        food_found = random.randint(0, 4)
        self.food += food_found
        self.dirtiness += 2
        print("\nThe creature found " + str(food_found) + "pieces of food")

    def show_values(self):
        """Display info"""
        print("\nCreature Name: " + self.name)
        print("Hunger (0-10): " + str(self.hunger))
        print("Boredom (0-10): " + str(self.boredom))
        print("Tiredness (0-10): " + str(self.tiredness))
        print("Dirtiness (0-10): " + str(self.dirtiness))
        print("Food Inventory: " + str(self.food) + " pieces")
        if self.is_sleeping:          
            print("Current Status: Sleeping")
        else:
            print("Current Status: Awake")

    def incriment_values(self, difficulty):
        """Defining the complexity"""
        self.hunger += random.randint(0, difficulty)
        if  not self.is_sleeping:
            self.boredom += random.randint(0, difficulty)
            self.tiredness += random.randint(0, difficulty)
        self.dirtiness += random.randint(0, difficulty)
            
    def kill(self):
        """The method describing death"""
        if self.hunger >= 10:
            print("\nThe creature is died of starvation")
            self.alive = False
        elif self.dirtiness >= 10:
            print("\nThe creature suffered an infection and died")
            self.alive = False
        elif self.boredom >= 10:
            self.boredom = 10
            print("\nThe creature is bored and falling asleep")
            self.is_sleeping = True
        elif self.tiredness >= 10:
            self.tiredness = 10
            print("\nThe creature is sleepy and falling asleep")
            self.is_sleeping = True
            
#Function block            
def show_menu(Creature):
    """Display user choices"""
    if Creature.is_sleeping:
        choice = input("\nEnter (6) to try and wake up:")
        choice = '6'
    else:
        print("\nEnter (1) to eat.")
        print("Enter (2) to play.")
        print("Enter (3) to sleep.")
        print("Enter (4) to take a bath.")
        print("Enter (5) to forage for food.")
        choice = input("What is your choice: ")
    
    return choice
        
def call_action(Creature, choice):
    if choice == '1':
        Creature.eat()
    elif choice == '2':
        Creature.play()
    elif choice == '3':
        Creature.sleep()
    elif choice == '4':
        Creature.clean()
    elif choice == '5':
        Creature.forage()
    elif choice == '6':
        Creature.awake()
    else:
        print("\nNon valid choce!!!")

#Main code
print("Welcome to the Pythonagachi Simulator App")

difficulty = int(input("\nPlease choose a difficulty level (1-5): "))
if difficulty > 5:
    difficulty = 5
elif difficulty < 1:
    difficulty = 1

plaing = True
while plaing:
    
    name = input("What name would you like to give your pet Pythonogachi: ").title().strip()
    my_pet = Creature(name)
    rounds = 1

    while my_pet.alive:
        print("\n----------------------------------------------------------------------------\nRound #" + str(rounds))
        my_pet.show_values()
        round_move = show_menu(my_pet)
        call_action(my_pet, round_move)

        print("\nRound #" + str(rounds) +" Summary:")
        my_pet.show_values()
        input("Press enter to continue")

        my_pet.incriment_values(difficulty)
        my_pet.kill()
        rounds += 1
    
    print("\nR.I.P.")
    print(name + " survived a total of " + str(rounds) + " rounds.")
    end_game = input("\nWould you like to play again (y/n): ").lower()
    if end_game == 'y':
        continue
    else:
        print("\nThank you for playing Pythonagachi!")
        plaing = False
