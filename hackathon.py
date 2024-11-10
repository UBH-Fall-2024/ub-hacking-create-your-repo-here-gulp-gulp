import time
import random
seconds=0
currentGame=""
money=200
gameOn=False
symbols = ['♡','♧','♤','♢','✧',]

payouts = {'♡':2,'⁠♧':3,'♤':5,'♢':10,'✧':15} 
    
spin_result=[]

#meant to simulate odds (not actually 50/50)
def fifty(LR):
    LR=False
    num=random.random()
    if(num<.45):
        return LR
    else:
        LR=True
        return LR
        #used for tower and sees if string is left or right or other
def decis(string):
    if(string.lower()=="left"):
        return 0
    elif(string.lower()=="right"):
        return 1
    else:
        return 2

#displays the games
def back():
    global gameOn
    print("balance: " + "$"+ str(round(money,2)))
    print("Games: slots, tower, cups, crash")
    gameOn=False
    time.sleep(.5)
    newGame()


#the game selector if you say yes you replay if no you go back to the games and anything else is not understood
def selector(word):
    if(word.lower()=="yes" and currentGame=="tower"):
        print("Balance: "+"$"+str(round(money,2)))
        tower()
    elif(word.lower()=="yes" and currentGame=="crash"):
        print("Balance: "+"$"+str(round(money,2)))
        crash()
    elif(word.lower()=="yes" and currentGame=="slots"):
        print("Balance: "+"$"+str(round(money,2)))
        spin_result=[]
        slot_machine_game()
    elif(word.lower()=="no"):
        print("")
        back()
    else:
        print("I couldn't quite understand could you type yes or no this time 😠")
        selector(input())

#function checks to see if the input is a real number
def isDigit(cash):
    try:
        float(cash)
        return True
    except ValueError:
        return False



#function to count seconds and every 10 seconds it will give $10


import random  # Import the random module for generating random percentages
import time  # Import time module to add a delay between rounds



            


#crash game 
def crash():
    global money
    blowout=False
    while(money>0 and blowout==False):
        print("How much would you like to spend: ")
        cash=input()
        if (not isDigit(cash)or float(cash)<0):
            print("not valid 😠")
            continue
        if(float(cash)>money):
            print("insufficient funds 😭")
            continue
        print("when do you want to crash out: ")
        out=input()
        if (not isDigit(out) or float(out)<0):
            print("not valid 😠")
            continue
        crashpercent=.00
        rand=random.random()
        percent=1.00
        for x in range(0,3):
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
                money=money-float(cash)
                money=money+float(new)
                time.sleep(1)
                print("play again? yes or no")
                selector(input())
                
            elif(round(crashpercent,2)>=round(crashout,2)):
                blowout=True
                print("Crashed out -_-")
                money=money-float(cash)
                time.sleep(1)
                print("play again? yes or no")
                selector(input())






def tower():
    global money
    fail=False
    while(money>0 and fail!=True):
        print("How much would you like to spend: ")
        cash=input()
        if (not isDigit(cash)or float(cash)<0):
            print("not valid 😠")
            continue
        if(float(cash)>money):
            print("insufficient funds 😭")
            continue
        trials=0
        tow=[]
        col=[]
        tempnum=7
        out=""
        for num in range(7,0,-1):
            tow.append([round(float(cash)*(1.5**num),2)])
            tow.append([round(float(cash)*(1.5**num),2)])
            col.append(tow)
            tow=[]
        for x in range(len(col)):
            print(col[x])
        while(fail==False):
            if(trials==0):
                print("Left or Right")
            else:
                print("Left, Right, or stop")
            decision=input()
            print("")
            print("")
            temp=decis(decision)
            if(decision.lower()=="stop"and trials>=1):
                print("Cashed out $"+str(out))
                money=round(money-float(cash),2)
                money=round(money+float(out),2)
                print("play again? yes or no")
                selector(input())
            if(decis(decision)==2 and trials==0):
                print("ENTER LEFT OR RIGHT 😡")
                continue
            elif(decis(decision)==2):
                print("ENTER LEFT, RIGHT, OR STOP")
                continue
            if(fifty(decision)==True):
                tempnum=tempnum-1
            else:
                col[tempnum-1][temp]="X"
                for x in range(len(col)):
                    print(col[x])
                print("")
                print("")
                print("yikes you lose 😭")
                money=round(money-float(cash),2)
                time.sleep(.3)
                print("play again? yes or no")
                selector(input())
            out=str(col[tempnum][temp])[1:-1]
            col[tempnum][temp]="✔"
            for x in range(len(col)):
                print(col[x])
            trials=trials+1
            
    
    



symbols = ['♡','♧','♤','♢','✧',]

payouts = {'♡':2,'⁠♧':3,'♤':5,'♢':10,'✧':15} 
    



def slot_machine_game() :
    global money,spin_result
    savespin=[]

    def spin_slot_symbols() :
        print("")
        time.sleep(.5)
        print("watashi wasta es spinning")
        print("")
        for y in range(0,3):
            spin_result=[]
            for x in range(0,3):
                spin_result.append(random.choice(symbols))
            time.sleep(.5)
            print(spin_result)
            savespin.append(spin_result[y])
        print("")
        time.sleep(1)
        print("Final Result")
        print(savespin)
        time.sleep(1)
        return savespin

    

    def check_win(spin_result, bet_amount):

        if(savespin[0]==savespin[1]==savespin[2]):
            if(savespin[0]=="♡"):
                return bet*2
            elif(savespin[0]=="⁠♧"):
                return bet*3
            elif(savespin[0]=="♤"):
                return bet*5
            elif(savespin[0]=="♢"):
                return bet*10
            elif(savespin[0]=="✧"):
                return bet*15
        else:
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
    spin_slot_symbols()
    winnings=check_win(savespin,bet)
    if(winnings==0):
        time.sleep(.5)
        print("You Lose!")
        money=money-bet
        time.sleep(.4)
        print("play again? yes or no")
        selector(input())
    else:
        time.sleep(.5)
        print("Wow you actually won $"+str(winnings))
        money=money-bet
        money=money+winnings
        time.sleep(.4)
        print("play again? yes or no")
        selector(input())
    

    














print("Welcome to gulp gulp casinos what would you like to play")
print("we have slots, tower, cups, and crash")


def newGame():
    global gameOn,currentGame
    while(gameOn==False):
        game=input("Enter a game: ")
        if(game.lower()=="crash"):
            currentGame="crash"
            gameOn=True
            crash()
        elif(game.lower()=="tower" or game.lower()=="towers"):
            currentGame="tower"
            gameOn=True
            tower()
        elif(game.lower()=="slot" or game.lower()=="slots"):
            currentGame="slots"
            gameOn=True
            slot_machine_game()
newGame()