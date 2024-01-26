import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)

    return roll
while True:
    players=input("Enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2 <=players <=4 :
            break
        else:
            print("Must be between 2-4 Players ")
    else:
        print("Invalid , Try again")


max_score=50
player_score=[0 for _ in range (players)]


while max(player_score)<=max_score:
    for i in range (players):
        print("\nPlayer",i+1,"it's your turn now !\n")
        print("Your total score is : ",player_score[i])
        current_score=0

        while(True):
            should_roll=input("Would you like to Roll (Y) ?")
            if should_roll.lower()!= "y":
                break
        
        
            value=roll()
            if value==1:
                print("You rolled a 1 ! Turn done !")
                current_score=0
                break
            else:
                current_score+=value
                print("You rolled a : ",value)
    
            print("Your current score is : ",current_score)
        
        player_score[i]+=current_score
        print("Your total score is : ",player_score[i])

max_score= max(player_score)
winning_index=player_score.index(max_score)
print("Player number",winning_index+1,"is the winner with a score of",max_score)
