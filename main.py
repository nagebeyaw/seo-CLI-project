
username= input("Enter your username: ").strip()

while True:
  print("\n ---Menu--- ")
  print("1. View Holdings")
  print("2. My Goal")
  print("3. Update/Upload Assets")
  print("4. Exit")

  number = input("\nSelect an option by entering 1-4:").strip()

  if choice == "1":
    holding = get_data(user)
    if holding == None:
      print("No holdings found. Upload assets first.")
    else:
      print()
      print("Your Holdings: ")
      print(Holdings)
  elif choice == "2":
    #call the goal function

  elif choice == "3":
    wallet = input("Enter your crypto wallet address: ").strip()
    #use the apis to get assets
    
    print("Assets Saved.")

  elif choice == "4":
    print("Goodbye!")
    break
  else:
    print("invalid option. Choose options 1-4.")

  

