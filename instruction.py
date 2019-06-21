def inst():
  print("======================= Instruction =======================")
  print("\nThe main goal of the game is to find Jon’s murderer. You do this by finding clues, and when you got enough clues, you can try to accuse a suspect.")

  print("\nYou can instructions at any time, by typing 'instructions' in the prompt filed")

  print("\nRooms and movement:")
  print("The main (central room), is Foyer. From this room, you go to every other room. So for example, if you are in the Main Hall, and you want to go to the kitchen, you have to type the: foyer (lowercase), and then when prompted what you want to do next, you going to type: the kitchen.")

  print("\nNames of the available rooms = ['foyer', 'main', 'study', 'kitchen', 'guest', 'bedroom', 'closet']")

  print("\nNames of the available people = ['Rob','Eric', 'Pennyworth', 'Sansa'  ]")


  print("\nConversation with people:")
  print("\nIn order to talk to somebody, you need to be in the Main Hall, because everyone is gathered there.")

  print("\nYou talk to somebody by typing: talk Name, for example, talk Eric (the first letter of the first name has to be capitalized)")

  print("\nGeneral interactions:")
  print("\nYou are able to interact with the items. Anytime you enter a room, there will instructions in parenthesis, by the named object. For example, when you walk into the kitchen, in the description of the kitchen you will see stow (examine stow), and in the parenthesis, there will be a command you need to type in the command line.")

  print("\nTo see the clues type: clues")
  print("To see inventory type: inventory")
  print("to see people, type: people")
  print("to see rooms type: rooms.")

  print("\nWeapons:")
  print("in this game, you can obtain 2 weapons, dagger and gun. You can use them only when attacked. You can do this by typing: use weapon name of the attacker. For example: use dagger Pennyworth")