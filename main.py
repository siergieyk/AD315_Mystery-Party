from yahtzee import *
from sortfind import *
from notepad import *
from binarySAC import *
from people import *
from perm import *
from end import *
from bst import *
from instruction import*
import numpy as np



print("Welcome to dinner at Baskerville, murder mystery party")
inst()


print("\n============================= Name =============================")
name = input("What's your name? :")

print("Hello",name)

print("")
print("\nReading a letter from the host")
print("\n============================= Letter =============================")
print("\nDear Friend,")
print("I can’t wait to see you. There are some thing I need to tell you.")
print("Jon")


print("\n============================= Mansion =============================")
print("\nBy the entrance, you were welcomed by security, you were searched for weapons, and your phone was confiscated. Jon was very particular when it came to his privacy, and none beside him was allowed to carry one.")

print("\nAs soon as you entered the foyer and were about to take your coat off, lights in the whole house went out, and you heard scream followed by a gurgling shriek.")

print("\nAfter a few seconds, all lights came back on, and you can see from foyer the host and your dear friend Jon is laying on the floor on his stomach in a puddle of blood, with the dagger in his back.")

print("\nThe security guard said that you were the last person to arrive, and the door will be locked behind you. It will be unlocked when the police arrives.")

rooms = ['foyer', 'main','study','kitchen','guest','bedroom','closet']

people = ['Rob','Eric', 'Pennyworth', 'Sansa'  ]

inventory = set()

Clues = set()

def MainHall():
  print("============================= Main Hall =============================")
  print("\nYou are in the Main Hall. All the people were gathered around Jon’s body (examine body), quietly staring at the body and each other.")
  print("\nYou see: Rob, Eric, Pennyworth, Sansa, Bran (You can interact with these people by typing 'talk' followed by the name, for example talk Rob")

  action=input("What you want to do in the main hall? :")
  if action == 'examine body':
    print("============================= Body Examination =============================")
    print("\nYour dear friend Jon is laying on the floor on his stomach in a puddle of blood, with the dagger in his back.")
    print("\nThe dagger that Jon was stabbed, was made of stainless steel. it had an approximately 8-inch blade, and approximately 6-inch handle. The dagger was seamlessly transferred from the blade into handle, without any visible transition elements, with any had guard. The handle was made of black obsidian.")
    print("\nSurprisingly the blade had a 10-inch string resembling dental floss attached to the end of its handle, with a small loop at the end.")
    print("\nAfter closer examination, you noticed that at the butt of the handle, there was a small etching 'SSA'. What does the 'SSA' stand for? Perhaps Stainless Steel, who knows?")
    print("\nIn Jon's pockets you found a cellphone, a notepad (use notepad), a key, a dagger (use dagger name).")
    print("\n These items were added to your inventory, you see items in the inventory by typing 'inventory'")
    inventory.add("cellphone(cellphone find),(sellphone sort)")
    inventory.add("notepad (use notepad)")
    inventory.add("Study Room key")
    inventory.add("dagger")

    Clues.add("dagger has engraved SSA")

    print("\nThe cell phone looked just like a regular phone, with two additional application: sort, and find (activate them by typing 'cellphone sort' and 'cellphone find').")
    print("\nPerhaps I should check the kitchen, to see if any knives are missing, or talk to sombody")

  if action == 'talk Eric':
    Eric()
  if action == 'talk Pennyworth':
    Pennyworth()
  if action == 'talk Rob':
    Rob()
  if action == 'talk Sansa':
    Sansa()

  if action == 'use notepad':
    Notepad()
  if action == 'clues':
    print("============================= Clues =============================")
    print(Clues)
  if action == 'rooms':
    print("============================= Rooms =============================")
    print(rooms)
  if action == 'people':
    print("============================= People =============================")
    print(people)
  if action == 'inventory':
    print("============================= Inventory =============================")
    print(inventory)
  if action == 'instructions':
    inst()


  if action == 'cellphone sort':
    print("============================= Cellphone Sort =============================")
    print("Do you want to sort the SafeCombo list?")
    sortAction=input("yes or no :")
    if sortAction == 'yes':
      SortedList=bubSortRec(list(SafeCombo))
      print("This is the sorted list: ",SortedList)
      print("According to the Jon's Notepad (examine notepad), there are some additional steps have to be taken in order to find the combination.")
      print("Now this list is stored in SortedList array")

  if action == 'cellphone find':
    print("============================= Cellphone Find =============================")
    num = input("Which number would you like to find? :")
    result = binarySearchRec(SortedList1, 0, len(SortedList1)-1, int(num))
    print(int(result))

  if action == 'accuse Pennyworth':
    print("============================= Pennyworth =============================")
    print("\nPennyworth: You are mistaken!")
  
  if action == 'accuse Eric':
    print("============================= Eric =============================")
    print("\nSansa: You can't be serious!")

  if action == 'accuse Sansa' and len(Clues)<10:
    print("============================= Sansa =============================")
    print("Sansa: You got nothing on me!")

  if action == 'accuse Sansa' and len(Clues)>=10:
    print("============================= Sansa =============================")
    print("\nSansa: Oh noooo!")
    print("\nSansa: It was all Rob's idea.")
    print("\nRob: Sansa and I, were planning this since we found out that Jon knew about us, and was going cut Sansa's funds!")
    print("\nRob turns around, leans his head back, and starts pulling out a string from his throat.")
    print("\nSuddenly you se a dagger coming out from his throat, the same dagger that was used to kill Jon.")
    print("\nWith dagger in his hand, Rob is charging at you!")
    defense = input("\nWhat's your move? :")
    if defense == 'use gun Rob' and 'gun' in inventory:
      print("You aim at Rob, and slowly squeeze trigger.")
      print("Rob's body slowly collapsed on the floor... ")
      end()
    if defense == 'use gun Rob' and 'gun' not in inventory:
      print("\nYou don't have a gun!")
      print("You got stabbed  in the heart, everything became blurry and dark.")
      end()
    if defense == 'use dagger Rob':
      print("\nYou were able to stab Rob, befor he stabbed you.")
      print("Rob's body slowly collapsed on the floor... ")
      end()

  if action == 'accuse Rob' and len(Clues)<10:
    print("============================= Rob =============================")
    print("You got nothing on me!")

  if action == 'accuse Rob' and len(Clues)>=10:
    print("============================= Rob =============================")
    print("\nRob: You got me!")
    print("\nRob: Sansa and I, were planning this since we found out that Jon knew about us, and was going cut Sansa's funds!")
    print("\nRob turns around, leans his head back, and starts pulling out a string from his throat.")
    print("\nSuddenly you se a dagger coming out from his throat, the same dagger that was used to kill Jon.")
    print("\nWith dagger in his hand, Rob is charging at you!")
    defense = input("\nWhat's your move? :")
    if defense == 'use gun Rob' and 'gun' in inventory:
      print("You aim at Rob, and slowly squeeze trigger.")
      print("Rob's body slowly collapsed on the floor... ")
    if defense == 'use gun Rob' and 'gun' not in inventory:
      print("\nYou don't have a gun!")
      print("You got stabbed  in the heart, everything became blurry and dark.")
      end()
    if defense == 'use dagger Rob':
      print("\nYou were able to stab Rob, befor he stabbed you.")
      print("Rob's body slowly collapsed on the floor... ")
      end()



  if action == 'foyer':
    room()
  else:
    MainHall()
    

def StudyRoom():
  print("============================= Study Room =============================")
  print("\nYou are in the Study Room, you see a big old desk with a computer on it and a picture")
  print("\nIn this room you can examine: Picture (examine picture), Computer (examine computer")
  action=input("What you want to do in the Study Room :")
  if action == 'examine picture':
    print("============================= Picture =============================")
    print("You see a picture of John with Sansa, on the frame is text 'Best Day Of my Life', and a date in the corner 04-12-86")
  if action == 'examine computer':
    print("============================= Examine Computer =============================")
    print("\nYou see 2 encrypted files, 'My last will' (examine will), when you click on it, you get an input filed for password, and text 'Remeber There are 10 types of people, the ones who understand binary, and those that don't', and you see 'Accounting Books' (examine accounting), when you click on this file, you get a prompt 'Remeber South Africa'")
    print("\nyou see two more applications on the computer: Decimal to Binary Conversion, and South Affrican Cypher (you can invoke these applications by typing 'use cypher' or 'use binary.) ")
  if action == 'examine will':
    print("============================= Will =============================")
    pcpass2=input('Password :')
    if pcpass2 == '1010000101000110':
      print("\n============== Will with today's date ==============")
      print("TLDR:Everything I have is going to be put in Eric's trust until he is 21 years old.")
      Clues.add("Sansa won't get any money according to the will")
  if action == 'examine accounting':
    print("============================= Accounting =============================")
    pcpass=input('Password :')
    if pcpass == '7698759763936098810':
      print("\n============== Accounting information ==============")
      print("TLDR:You see plenty transfers from Napier investments in Gotham city, into his offshore accounts")
      Clues.add("Transfers from Nappier Investments")
  if action == 'use binary':
    print("============================= Binary =============================")
    num=input("Enter your number :")
    dec2bin(num)
    StudyRoom()
  if action == 'use cypher':
    print("============================= South African Cypher =============================")
    word=input("Enter your phrase :")
    saspc(word.lower())
    StudyRoom()

  if action == 'use notepad':
    Notepad()
  if action == 'clues':
    print("============================= Clues =============================")
    print(Clues)
  if action == 'rooms':
    print("============================= Rooms =============================")
    print(rooms)
  if action == 'people':
    print("============================= People =============================")
    print(people)
  if action == 'inventory':
    print("============================= Inventory =============================")
    print(inventory)
  if action == 'instructions':
    inst()

  if action == 'cellphone sort':
    print("============================= Cellphone Sort =============================")
    print("Do you want to sort the SafeCombo list?")
    sortAction=input("yes or no :")
    if sortAction == 'yes':
      SortedList=bubSortRec(list(SafeCombo))
      print("This is the sorted list: ",SortedList)
      print("According to the Jon's Notepad (examine notepad), there are some additional steps have to be taken in order to find the combination.")
      print("Now this list is stored in SortedList array")

  if action == 'cellphone find':
    print("============================= Cellphone Find =============================")
    num = input("Which number would you like to find? :")
    result = binarySearchRec(SortedList1, 0, len(SortedList1)-1, int(num))
    print(int(result))
  if action == 'foyer':
    room()
  else:
    StudyRoom()


def Kitchen():
  print("============================= Kitchen =============================")
  print("\nThe kitchen seemed to be rather normal, it had cabinets with matching drawers (examine drawers), a stove (examine stow), fridge (examine fridge), and an island in the center for meal preparation. Under the island was a trashcan.(examine trashcan)")
  action=input("What you want to do in the Kitchen? :")
  if action == 'examine trashcan':
    print("============================= Trashcan =============================")
    print('\nIn the trashcan you found an envelope addressed to Pennyworth. The return address stated B.W. Gotham City.')
    Clues.add("Pennyworth is from Gotham City")
  if action == 'examine fridge':
    print("============================= firdge =============================")
    print("\nKnives and all the utensils, in the drawers, were of great quality, but none of them were missing or resembling the one that used to kill Jon.")
  if action == 'examine stow':
    print("============================= Stow =============================")
    print("\nThere is some paper ash, seems that something may have been burned. You see onyl a small piece of paper that wasn't burned that says '....acording to plan.'")
    Clues.add("Burned letter in the Kitchen")


  if action == 'use notepad':
    Notepad()
  if action == 'clues':
    print("============================= Clues =============================")
    print(Clues)
  if action == 'rooms':
    print("============================= Rooms =============================")
    print(rooms)
  if action == 'people':
    print("============================= People =============================")
    print(people)
  if action == 'inventory':
    print("============================= Inventory =============================")
    print(inventory)
  if action == 'instructions':
    inst()

  if action == 'cellphone sort':
    print("============================= Cellphone Sort =============================")
    print("Do you want to sort the SafeCombo list?")
    sortAction=input("yes or no :")
    if sortAction == 'yes':
      SortedList=bubSortRec(list(SafeCombo))
      print("This is the sorted list: ",SortedList)
      print("According to the Jon's Notepad (examine notepad), there are some additional steps have to be taken in order to find the combination.")
      print("Now this list is stored in SortedList array")

  if action == 'cellphone find':
    print("============================= Cellphone Find =============================")
    num = input("Which number would you like to find? :")
    result = binarySearchRec(SortedList1, 0, len(SortedList1)-1, int(num))
    print(int(result))
  if action == 'foyer':
    room()
  else:
    Kitchen()


def GuestRoom():
  print("============================= Guest Room =============================")
  print("\nIt is a generic guest room, and a single queen-sized bed, a desk (examine desk), and a walk-in closet, and a private bathroom.")
  print("\nThis is the room where Rob is staying. In the corner, there is carryon suitcase (examine suitcase).")
  action=input("What do you want to do in the Guest Room? :")
  if action == 'examine desk':
    print("============================= Desk =============================")
    print("\nNothing special about the desk, but you noticed the newest edition Sword Swallowers Association magazine. It probably belongs to Rob.")
    Clues.add("Rob reads Sword Swallowers Association Magazine")
  if action == 'examine suitcase':
    print("============================= Suitcase =============================")
    print("\nYou see Rob's clothes")
    print("\nYou found a note in the side pocket 'I know what you are doing, and I want you to stop.' Signed Jon.")
    Clues.add("Jon sent a letter to Rob, requesting him to stop doing something....")
  
  if action == 'use notepad':
    Notepad()
  if action == 'clues':
    print("============================= Clues =============================")
    print(Clues)
  if action == 'rooms':
    print("============================= Rooms =============================")
    print(rooms)
  if action == 'people':
    print("============================= People =============================")
    print(people)
  if action == 'inventory':
    print("============================= Inventory =============================")
    print(inventory)
  if action == 'instructions':
    inst()

  if action == 'cellphone sort':
    print("============================= Cellphone Sort =============================")
    print("Do you want to sort the SafeCombo list?")
    sortAction=input("yes or no :")
    if sortAction == 'yes':
      SortedList=bubSortRec(list(SafeCombo))
      print("This is the sorted list: ",SortedList)
      print("According to the Jon's Notepad (examine notepad), there are some additional steps have to be taken in order to find the combination.")
      print("Now this list is stored in SortedList array")

  if action == 'cellphone find':
    print("============================= Cellphone Find =============================")
    num = input("Which number would you like to find? :")
    result = binarySearchRec(SortedList1, 0, len(SortedList1)-1, int(num))
    print(int(result))

  if action == 'foyer':
    room()
  else:
    GuestRoom()


def BedRoom():
  print("============================= Bedroom =============================")
  print("\nIt is a typical bedroom with bed with headrest against the wall and nightstands on each side (examine nightstand). Farther in the room, there is a walk-in closet (examine closet).")

  print("\nHere Jon and Sansa spent their nights. Jon used to sleep on the left side, and Sansa slept on the right side. ")

  action=input("What do you want to do in the Bedroom? :")
  if action == 'examine nightstand':
    print("============================= Nightstand =============================")
    print("\nOn Sansa’s side of the bed, in the nightstand you found a letter,'Remember about the surprise, and turn the lights off as soon as the door closes behind the last guest, Pennyworth will bring the cake, while it’s dark', Signed R.")
    print("You: Can R stand for Rob?")
    Clues.add("Suspicious note to Sansa from R. about the surprise")
  
  if action == 'use notepad':
    Notepad()
  if action == 'clues':
    print("============================= Clues =============================")
    print(Clues)
  if action == 'rooms':
    print("============================= Rooms =============================")
    print(rooms)
  if action == 'people':
    print("============================= People =============================")
    print(people)
  if action == 'inventory':
    print("============================= Inventory =============================")
    print(inventory)
  if action == 'instructions':
    inst()

  if action == 'cellphone sort':
    print("============================= Cellphone Sort =============================")
    print("Do you want to sort the SafeCombo list?")
    sortAction=input("yes or no :")
    if sortAction == 'yes':
      SortedList=bubSortRec(list(SafeCombo))
      print("This is the sorted list: ",SortedList)
      print("According to the Jon's Notepad (examine notepad), there are some additional steps have to be taken in order to find the combination.")
      print("Now this list is stored in SortedList array")

  if action == 'cellphone find':
    print("============================= Cellphone Find =============================")
    num = input("Which number would you like to find? :")
    result = binarySearchRec(SortedList1, 0, len(SortedList1)-1, int(num))
    print(int(result))

  if action == 'examine closet':
    Closet()
  if action == 'foyer':
    room()
  else:
    BedRoom()


def Closet():
  print("============================= Closet =============================")
  print("\nYou are in the closet.")
  print("\nIn the closet, you can see Jon’s and Sansa’s clothes, and Jon’s safe (examine safe) with the keypad.")
  action=input("What you want to do in the closet? :")
  
  if action == 'use notepad':
    Notepad()
  if action == 'clues':
    print("============================= Clues =============================")
    print(Clues)
  if action == 'rooms':
    print("============================= Rooms =============================")
    print(rooms)
  if action == 'people':
    print("============================= People =============================")
    print(people)
  if action == 'inventory':
    print("============================= Inventory =============================")
    print(inventory)
  if action == 'instructions':
    inst()

  if action == 'cellphone sort':
    print("============================= Cellphone Sort =============================")
    print("Do you want to sort the SafeCombo list?")
    sortAction=input("yes or no :")
    if sortAction == 'yes':
      SortedList=bubSortRec(list(SafeCombo))
      print("This is the sorted list: ",SortedList)
      print("According to the Jon's Notepad (examine notepad), there are some additional steps have to be taken in order to find the combination.")
      print("Now this list is stored in SortedList array")
    
  if action == 'cellphone find':
    print("============================= Cellphone Find =============================")
    num = input("Which number would you like to find? :")
    result = binarySearchRec(SortedList1, 0, len(SortedList1)-1, int(num))
    print(int(result))

  if action == 'examine safe':
    print("============================= Safe =============================")
    combination = input("Enter your combination :")
    if combination == '34213942':
      print("you found a gun and Jon's will")
      print("\n============== Jon's will dated 2 years ago ==============")
      print("TLDR: Everything goes to Sansa")
      inventory.add('gun')
      print("Gun has been added to your inventory (use gun name).")
      print("\nYou went back to the bedroom.")
    else:
      Closet()
  else:
    BedRoom()


def Eric():
  print("============================= Eric =============================")
  print("You approached Eric, Jon’s only son. He is sitting by himself in the corner of the room, while everyone is staring Jon’s body.")
  print("Hello",name,", it's nice to meet you")
  print("You: How is everything going ?")
  print("Eric: Would you like to play a round of Yahtzee with me?")
  yahtzee=input("yes or no? :")
  if yahtzee=='yes':
    print("Rob's result")
    Yahtzee()
    print(name+"'s result")
    Yahtzee()
    print("Thank you for the game, Rob would play with me when dad was on his business trips to Gotham")
    Clues.add("Rob visits Sansa, when Jon was on business trips.")
    MainHall()

def Sansa():
  print("============================= Sansa =============================")
  print("\nYou: Do you know who may have done this?")
  print("\nSansa: Hard to say, you may be the only person in this room who hasn’t hated Jon.")
  print("\nYou: Why is that?")
  print("\nSansa: He spent most of his time working for Jack Napier, in Gotham. He was practically his right hand.")
  Clues.add("Jon worked fro Jon Napier in Gotham City.")
  print("\nYou in Sansa's hand three cards that she's continously shuffling")
  print("\nYou: What about these cards?")
  print("\You: nYou seem nervous")
  print("\nSansa: I'm just trying to fugre out all the possible combinations for these three cards.")
  print(faceHearts)
  print("\nSansa: Would you help me?")
  print("Sansa asked with a shaky voice....")
  cards = input ("yes or no? :")
  if cards == 'yes':
    perm()
  print("\nSansa: Thank, thank you!")
  print("Sansa was continously repeating.")
  MainHall()

def Rob():
  print("============================= Rob =============================")
  print("\nYou: Hey Rob, long time no see. How is everything going?")
  print("\nRob: I’m definitely better than Jon.")
  print("\nYou: Do you know anything about what happened here?")
  print("\nRob: Hard to say, but based on my experience, it’s always the butler.")
  Clues.add("Rob thinks it might have been Pennyworth")
  print("Rob: I would talk to this Pennyworth guy; he seems suspicious to me.")
  MainHall()

def Pennyworth():
  print("============================= Pennyworth =============================")
  print("\nYou: So, what do you think has happened here?")
  print("\nPennyworth: Hard to say, and it’s not polite to gossip.")
  print("Pennyworth: But Lady Sansa, would go to the bedroom, late at night, and somehow, I see her sneaking into the house early in the morning.")
  Clues.add("Sansa would sneak out at night.")
  print("\nPennyworth: I haerd that you have some programming experice. Would care to help me with the Binary Search Tree?")
  action = input("yes or no :")
  if action == 'yes':
    print("Pennyworth: Great! here is the tree in preorder:")
    pre()
    print("Pennyworth: Is it balanced ? :")
    action = input("yes or no :")
    if action == 'yes':
      print("Pennyworth: I don't know.....")
    if action == 'no':
      print("Pennyworth: So I thought... Maybe if I add these nummber?")
      print(arrayBalance)
      print("Pennyworth: Do you think this would work? ")
      action = input("yes or no :")
      if action == 'yes':
        print("Pennyworth: Let's try it!")
        preorder(r)
        print("Thank you!")
        print("Pennywort: (whispering) for your help, I will give you a hit....  ")
        print("Check safe located in the bedroom's closet...")

  MainHall()

def room():
  print("============================= Foyer =============================")
  print(rooms)
  action=input("\nYou are in the Foyer, where would you like to go? :")
  print()
  if action =='main':
    return MainHall()
  if action =='study' and 'Study Room key' in inventory :
    return StudyRoom()
  else:
    print("The Study Room door is locked")
  if action =='kitchen':
    return Kitchen()
  if action =='guest':
    return GuestRoom()
  if action =='bedroom':
    return BedRoom()
  if action =='closet':
    return Closet()
  else:
      room()

room()





