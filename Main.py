'''this is main'''

from Rounds import play_round

def main():
    """our main funcion that will be able to run the game from several files"""
    
    print ("Gin Rummy! \nCreated By: Landree Allen & Madeleine Lucas")
    
    player_name = input("Name: ")
    
    while True:
        print("\nNew Round:\n")

        winner, player_deadwood, ai_deadwood = play_round(player_name)

        print("\n--- Round Results ---")
        print("Your deadwood:", player_deadwood)
        print("Computer deadwood:", ai_deadwood)
        
        if winner == "player":
            print("You won the round!")
        else:
            print("GinBot won the round.")

        again = input("\nPlay another round? y/n: ").lower()
        if again == "n":
            break
        
if __name__ == "__main__":
    main()