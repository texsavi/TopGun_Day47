import random, time, os


topGunns={}
list=["Maverick","Rooster","Goose","Bob","Hangman"]
topGunns["Maverick"]={"Rating": 5, "Jet": 18, "TopCruise": 11,  "MIGs taken": 12 }
topGunns["Hangman"]={"Rating": 4.4, "Jet": 18, "TopCruise": 8,  "MIGs taken": 7 }
topGunns["Goose"]={"Rating": 4.8, "Jet": 15, "TopCruise": 9,  "MIGs taken": 9}
topGunns["Rooster"]={"Rating": 4.5, "Jet": 18, "TopCruise": 10,  "MIGs taken": 7 }
topGunns["Bob"]={"Rating": 4.3, "Jet": 18, "TopCruise": 10,  "MIGs taken": 9}


while True:
  space=""
  print(f"{space:^20}\033[33m***Top Gun'ns***")
  print()
  print("Here's our Top Guns to fly with!...")
  print()
  
  for key in topGunns:
    print(key)
  print()
  cap=input("Pick your TopGun:\n >>> ")
  if cap not in list:
    print("Not a Top Gun")
    exit()
    
  comp=random.choice(list)
  print()
  print(f"The computer chooses {comp}")

  print()
  gunns=input("Select your gunns stats:\n1. Rating\n2. Jet\n3. TopCruise\n4. MIGs taken\n >>> ")
  
  print()
  print(f"{cap}: {topGunns[cap][gunns]}")
  print(f"{comp}: {topGunns[comp][gunns]}")

  print()
  if topGunns[cap][gunns] > topGunns[comp][gunns]:
    print(f"\033[32mWooohoo!! ***{cap}*** got more wings!\033[31m")
  elif topGunns[cap][gunns] < topGunns[comp][gunns]:
    print(f"\033[31mLooks like ***{comp}*** wings this!\033[1m")
  else:
    print("\033[34mYou'll both make amazing wingmen!\033[1m")

  time.sleep(4)
  os.system("clear")