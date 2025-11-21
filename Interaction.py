def show_hand(label, hand):
    '''prints cards and their index number
    EX Your hand: [0:A♠] [1:7♥] [2:7♣]'''
    
    print(label)
    
    i = 0
    while i < len(hand):
        card = hand[i] 
        print(str(i) + ":" + card)
        i = i + 1
    print("\n")
   
  

def show_top_of_discard(discard):
    '''prints the top card or says empty'''
    if len(discard) > 0:
        print("Top of discard:", discard[-1])
    else:
        print("empty")

  
  
def ask_choice(prompt, options):
    '''shows options Draw deck, Take discard, and return the chosen number'''
    while True:
        print(prompt)
        
        for key in options:
            print(key, ":", options[key])
            
        my = input(">")
        
        if my in options:
            return(my) #there is a chance this will not print my correctly
        
        print("Invalid.\n")



def ask_index(prompt, limit):
    '''asks for a number and return it this tells us which card to discard'''
    while True:
        print(prompt)
        print("You can only pick a number between 0 and", limit - 1)
        i = input(">")
         
    '''makes sure input is a digit'''
    if i.isdigit():
        num = int(i)
        if 0 <= num < limit:
            return num
    else:    
        print("Invalid index.")