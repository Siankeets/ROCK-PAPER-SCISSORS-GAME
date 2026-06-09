# ROCK PAPER SCISSORS
# Menu
#---- user pick an option  / 
#---- system randomnly picks option   / 
#---- fight rock>scissor>paper>rock    / 
#---- history of matches (maybe in txt file)  
#---- use machine learning maybe for prediction of next system move  
#---- create statistic for % of picked options

import random

startChecker = False
user_option = ""
bot_option = ""
options = ("ROCK", "PAPER", "SCISSOR")
startChecker2 = True
num = 1

class func():
    
    def invalidmsg(self):
        print(" ")
        print("This option is not valid, to enter the fight, please type the right option!")
        print("                     ROCK   /  PAPER  /  SCISSOR")
        print(" ")
        
    def invalidmsg2(self):
        print(" ")
        print("This option is not available, please type Y or N!")
        print(" ")
        
    def exitmsg(self):
        print(" ")
        print("         Thank you for using the app!")
        print("                 Exiting....")
        print("=" * 50)

    def conmsg(self):
        print(" ")
        print("Would you like to play again? Y/N")
        answer = input(": ")
        answer = answer.upper()
        answer = answer.strip()
        return answer

    def resultMaker(self, u_option, b_option):
        try:
            if u_option in options and b_option in options:
                match u_option:
                    case "ROCK": 
                        self.rock(u_option, b_option)
                    case "PAPER":
                        self.paper(u_option, b_option)
                    case "SCISSOR":
                        self.scissor(u_option, b_option)
            else:
                invalidmsg()
        except:
            invalidmsg()

    def rock(self, u_option, b_option):
        try:
            if u_option == "ROCK" and b_option == "SCISSOR":
                print("You won the fight!")

            elif u_option == "ROCK" and b_option == "ROCK":
                print("It's a tie!")

            else:
                print("You lost...")
        except:
            invalidmsg()

    def scissor(self, u_option, b_option):
        try:
            if u_option == "SCISSOR" and b_option == "PAPER":
                print("You won the fight!")

            elif u_option == "SCISSOR" and b_option == "SCISSOR":
                print("It's a tie!")

            else:
                print("You lost...")

        except:
            invalidmsg()

    def paper(self, u_option, b_option):
        try:
            if u_option == "PAPER" and b_option == "ROCK":
                print("You won the fight!")

            elif u_option == "PAPER" and b_option == "PAPER":
                print("It's a tie!")
                
            else:
                print("You lost...")

        except:
            invalidmsg()
            
    def main(self, checker, num):
        while checker:
            print("=" * 50)
            print(" ")
            
            print(f"              ROUND {num} ")
            print("         PICK YOUR FIGHTER!      ")
            print("    ROCK   /  PAPER  /  SCISSOR ")
            print(" ")
            user_option = input (": ")
            user_option = user_option.upper()
            user_option = user_option.strip()
            bot_option = random.choice(options)
            
            if user_option in options:
                print(f"Your fighter:   {user_option}")
                print(f"Bot's fighter:  {bot_option}")
                print(" ")
                self.resultMaker(user_option, bot_option)
                
                checker2 = True
                while checker2:
                    x = self.conmsg()
                    print(" ")
                    if x == "Y":
                        checker2 = False
                        num += 1
                        break
                    elif x == "N":
                        self.exitmsg()
                        exit()
                    else:
                        self.invalidmsg2()
                
            else:
                self.invalidmsg()
    
#MAIN
f = func()
while startChecker2:
    print("=" * 50)
    print(" ")
    print("         PLAY ROCK, PAPER, SCISSORS!     ")
    startup = input("       Would you like to play? (Y/N): ")
    print(" ")
    answer = startup.upper()
    answer = answer.strip()
    if answer == "Y":
        startChecker = True
        f.main(startChecker, num)
        
    elif answer == "N":
        f.exitmsg()
        startChecker2 = False
    else:
        f.invalidmsg2()