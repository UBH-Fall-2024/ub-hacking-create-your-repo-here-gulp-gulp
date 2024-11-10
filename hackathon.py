import time
seconds=0 
money=0
import random
#money input by user
def money_input():
    money_input=input("Bet Amount")
    return money_input



#function to count seconds and every 10 seconds it will give $10
def count_sec():
    global seconds,money
    while(seconds!=12):
        time.sleep(1)
        seconds=seconds+1
        if(seconds%10==0):
            money+=10
            seconds=0
            print("money: " + str(money))
count_sec()

import random  # Import the random module for generating random percentages
import time  # Import time module to add a delay between rounds

def random_percent_turn(ogpercent=50, rate_decay=1.9, rounds):  
    current_percent = ogpercent  
    for turn in range(rounds):  # Loop through each round up to the specified number of rounds
        if current_percent <= 0:  
            print("Game has ended.")  #percentage reached zero
            break  # Exit the loop if current_percent is zero or less

        percent = random.randint(0, int(current_percent))  
        print(f"Round {turn + 1} - Current random percent: {percent}%")  #current round and  percentage

        current_percent -= rate_decay ** 2  

        time.sleep(1)  # Pause for 1 second to simulate time between rounds



def cups(number_cups):
    while True:
        try:
            number_cups = int(input("Choose number of cups (2, 3, or 4): "))
            '''there is a _ amount of cups and random percent turn makes it so that 
            whatever number the user chooses, there is a chance the number contains a ball
            (win) and a chance there isnt a ball(lose) and it uses the random_percent_turn
             function to make it so the chance gets smaller and smaller each turn '''
             choice=input("write 1,2,3 or 4")
             if choice=True:
            random_percent_turn()
            
            if number_cups in [2, 3, 4]:
                output_mult = number_cups
                print(f"Output multiplier is set to: {output_mult}")
            else:
                print("WRITE A DAMN NUMBER")
            input(1,2,3,4)
            

def isDigit(cash):
    try:
        float(cash)
        return True
    except ValueError:
        return False

def crash():
    global money
    blowout=False
    while(money>0 and blowout==False):
        print("How much would you like to spend: ")
        cash=input()
        if not isDigit(cash):
            print("not valid")
            continue
        if(float(cash)>money):
            print("insufficient funds")
            continue
        print("when do you want to crash out: ")
        out=input()
        if not isDigit(out):
            print("not valid")
            continue
        crashpercent=.00
        rand=random.random()
        percent=1.00
        money=money-float(cash)
        for x in range(0,2):
            rand=random.random()
            if(round(rand,2)>round(crashpercent,2)):
                crashpercent=rand
        crashout=.96
        time.sleep(1)
    
        while(blowout!=True):
            if(percent<3):
                percent=percent*(1+(random.randint(1,5)/100))
                crashout=crashout*.992
            elif(percent>3 and percent<10):
                percent=percent*(1+(random.randint(5,10)/100))
                crashout=crashout*.98
            elif(percent>10 and percent<50):
                percent=percent*(1+(random.randint(10,15)/100))
                crashout=crashout*.965
            elif(percent>50 and percent<200):
                percent=percent*(1+(random.randint(15,20)/100))
                crashout=crashout*.945
            else:
                percent=percent*1.25
                crashout=crashout*.92
            new=float(cash)*percent
            time.sleep(.4)
            print("multiplier: " + str(round(percent,2)))
            print("$"+str(round(new,2)))
            if(percent>=float(out)):
                blowout=True
                print("Cashed out: " +str(round(new,2)))
                money+=float(out)
                
            elif(round(crashpercent,2)>=round(crashout,2)):
                blowout=True
                print("Crashed out -_-")
        

        
        

#tower game
def tower(money_input):
    multiplier=1.25
    total_Earnings=0
    level=0
    resultsList=[]
    for i in range(0,9):
        randomNumberTower=random.randint(1,2)
        resultsList.append(randomNumberTower)
    



symbols = ['♡','♧','♤','♢','✧',]

payouts = {'♡':2,'⁠♧':3,'♤':5,'♢':10,'✧':15} 
    



def slot_machine_game() :

    


    def spin_slot_symbols() :

        return [random.choice(symbols) for sym in range(3)]

    def display_spin(spin_result):

        print("watashi wasta es spinning")
        print(f"{spin_result[0] | spin_result[1] | spin_result[2]}")

    def check_win(spin_result, bet_amount):

        if len(set(spin_result)) == 1 :
            symbol = spin_result[0]
        if symbol in payouts:
            payout = bet_amount * payouts[symbol]
            return payout
        return 0
    


print("Welcome to slot tuah spin that thang")


while True:
        try:
            bet = int(input("Enter your bet amount: $"))
            if bet <= 0:
                print("Bet amount must be greater than 0. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for your bet.")
    

    

















