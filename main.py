# imports
import time, random

# Variables
warexhaustion = 1
enemyexhaustion = 1
enemycasualties = 0
friendlycasualties = 0
equipment = 10000

# Introduction + Instructions
print("You are currently in the battlefield in the Napoleonic Wars, you are currently facing the Austrians as a Frenchmen, you have 10000 men, while the Austrians has 10000 men too.")
print("NOTICE: THIS GAME CAN BE REALLY HARD OR REALLY EASY DEPENDING ON YOUR LUCK(RNG)")
time.sleep(2)
print(" ")
print("WINNING CONDITIONS")
print("If you inflict over 8000 casualties on the enemy or you make the enemy exhaustion level to 11, you will win.")
time.sleep(2)
print(" ")
print("LOSING CONDITIONS")
print("If you have over 8000 casualties, have no equipment or your warexhaustion is over 11, you lose")

while(True):
  time.sleep(2)
  # Decision Statements
  fieldinput = input("A. Flank Right \n"
  "B. Flank Left \n"
  "C. Charge Center \n"
  "D. Wait for more supplies\n"
  "E. Rest your army\n")
  if(fieldinput == "A" or "B" or "C" or "D" or "E"):
    if(fieldinput == "D"):
      print("You have decided to wait for more supplies")
      warexhaustion -= random.randint(1,2)
      equipment += random.randint(250, 1000)
      attackchance = random.randint(1,2)
      if(attackchance == 2): 
        print("The enemy has attacked you back!")
        friendlycasualties += random.randint(100, 200)
        enemycasualties += random.randint(1, 100) 
      print("You have " + str(friendlycasualties)+ " casualties")
      print("You have " + str(equipment) + " equipment")
       
    elif(fieldinput == "E"):
      print("You have decided to rest your army") 
      warexhaustion -= random.randint(1,11)
      equipment += random.randint(1, 50)
      attackchance = random.randint(1,2)
      if(attackchance == 2): 
        print("The enemy has attacked you back!")
        friendlycasualties += random.randint(100, 200)
        enemycasualties += random.randint(1, 100) 
      print("You have " + str(friendlycasualties)+ " casualties")
      print("You have " + str(equipment) + " equipment")

    elif(fieldinput == "A" or "B" or "C"):
      tacticalinput = input("A. Commit to a suicide charge(Only Available if you have 7500 casulties, and you have a high warexhaustion(5))\n"
      "B. Shell them\n"
      "C. Cavalry Charge\n"
      "D. Bayonet Charge\n"
      "E. Guerilla Warfare\n")

      if(tacticalinput == "A" and friendlycasualties >= 7500 and warexhaustion):
        print("You have decided to commit to a suicide charge in a last of desperation")
        warexhaustion += random.randint(5,11)
        friendlycasualties += random.randint(500, 1000)
        enemycasualties += random.randint(100,300)
        equipment -= random.randint(500, 1000)
        enemyexhaustion += 1
        print("You have " + str(friendlycasualties)+ " casualties")
        print("You have " + str(equipment) + " equipment")
        continue 
    
      if(tacticalinput == "B"):
        print("You have decided to shell them")
        shellchance = random.randint(1,2)
        warexhaustion += 1
        enemycasualties += random.randint(300, 400)
        equipment -= random.randint(0, 30)
        if(shellchance == 2):
          print("The enemy has attacked you back!")
          friendlycasualties += random.randint(100, 200) 
        print("You have " + str(friendlycasualties)+ " casualties")
        print("You have " + str(equipment) + " equipment")
        continue

      if(tacticalinput == "C"):
        print("You have decided to Charge them with mass amounts of Cavalry")
        warexhaustion += 1
        friendlycasualties += random.randint(100, 300)
        enemycasualties += random.randint(100,300)
        equipment -= random.randint(50, 100)
        enemyexhaustion += 1
        print("You have " + str(friendlycasualties)+ " casualties")
        print("You have " + str(equipment) + " equipment")
        continue
    
      if(tacticalinput == "D"):
        warexhaustion += 1
        friendlycasualties += random.randint(400, 500)
        enemycasualties += random.randint(400, 500)
        equipment -= random.randint(50, 100)
        enemyexhaustion += 1
        print("You have decided to start a Bayonet Charge with the infantry")
        print("You have " + str(friendlycasualties)+ " casualties")
        print("You have " + str(equipment) + " equipment")
        continue

      if(tacticalinput == "E"): 
        warexhaustion += 1
        friendlycasualties += random.randint(100, 150)
        enemycasualties += random.randint(200, 250)
        equipment -= random.randint(25, 50)
        enemyexhaustion += 1
        print("You have decided to not fight their ground, and go into the trees to shoot them")
        print("You have " + str(friendlycasualties) + " casualties")
        print("You have " + str(equipment) + " equipment")
        continue
    
    # Warnings
    if(warexhaustion >= 7):
      print("Your army is too exhausted! You need to rest them commander!")
    if(friendlycasualties >= 4500):
      print("Your casualties is too high, you need to be cautious commander!")
    if(enemycasualties >= 4500):
      print("Your enemy is too weak, you must attack at once commander!") 
    if(equipment <= 1000):
      print("Your equipment is low, you need to wait for your next supply train commander!")
    if(equipment <= 1 and warexhaustion == 10 and friendlycasualties == 7999 and enemycasualties == 1): 
      print("Your really bad at commanding aren't you?")
    

    # Winning and Losing Statements
    if(equipment == 0 or warexhaustion == 11 or friendlycasualties == 8000):
      print("You have lost to the Austrians\n"
      "Napoleon has decided to court-martial you personally for losing to the Austrians\n"
      "Y O U    H A V E   D I E D")
      break
    if(enemyexhaustion == 11 or enemycasualties == 8000):
      print("You are celebrated for your crushing victory on the Austrians\n"
      " Y O U   H A V E   W O N")
      break
  else:
    print("Please put a valid input")

# Ending
print("Thank you for playing this trash game!")
# easter egg
time.sleep(420)
print("big nerd you have waited 7 minutes to find this")
time.sleep(2)
print("your bad")