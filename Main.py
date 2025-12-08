'''this is main'''


from Rounds import play_round
from Interaction import engine



def main():

    player_name = "Player"

    while True:
        winner, p_dead, ai_dead = play_round(player_name)

        engine.clear_messages()
        engine.show_message(f"Round Over! Winner: {winner}")
        engine.show_message(f"Player Deadwood: {p_dead}", 60)
        engine.show_message(f"AI Deadwood: {ai_dead}", 90)

        engine.wait_for_click()

    engine.close()
        
if __name__ == "__main__":
    main()