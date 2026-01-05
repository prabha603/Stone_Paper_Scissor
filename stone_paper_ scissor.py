import random
print("------------------------------\n"
      "\t Game Rules\n"
      "------------------------------\n"
      "stone vs scissor -> stone wins\n"
      "scissor vs paper -> scissor wins\n"
      "paper vs stone   -> stone wins\n"
      "------------------------------\n")
user_name=input("Enter players name:")

count=0
count_of_tie=0
count_of_computer_won=0
count_of_player_won=0
while True:
    count=count+1
    
    
    games=["stone","scissor","paper"]
    random_games=random.choice(games)
   # user_1=random_games
    
    while True:
            user_2=input("Enter the players input(stone/scissor/paper) : ")
            if user_2  not in games:
                print("Invalid input!.Provide stone/scissor/paper")
                continue
            else:
                break
      
    if user_1==user_2:
        count_of_tie=count_of_tie+1
        print("match is tie")
    else: 
        if user_1=="scissor":
            if user_2=="stone":
                count_of_player_won=count_of_player_won+1
                print(user_name,"won")
            elif user_2=="paper":
                count_of_computer_won=count_of_computer_won+1
                print("computer won")
        if user_1=="paper":
            if user_2=="scissor":
                count_of_player_won=count_of_player_won+1
                print(user_name,"won")
            elif user_2=="stone":
                count_of_computer_won=count_of_computer_won+1
                print("computer won")
        if user_1=="stone":
            if user_2=="paper":
                count_of_player_won=count_of_player_won+1
                print(user_name,"won")
            elif user_2=="scissor":
                count_of_computer_won=count_of_computer_won+1
                print("computer won")
    print("computer selected", random_games)    
    print("Do you want to play again?(Y/N)")
    ans=input().lower()
    if ans =='n':
       break
print("------------------------------------------------------------")
print("\t\t Final Results")
print("------------------------------------------------------------")
print("Total number of games played:",count)
print("Total number of games tie:",count_of_tie)
print("Total number of games computer won:",count_of_computer_won)     
print("Total number of games",user_name,"won:",count_of_player_won) 
print("------------------------------------------------------------\n")  
print("Thanks for Playing") 