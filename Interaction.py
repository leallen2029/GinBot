'''interactions'''

from SetUp import organize_hand
from GameGraphics import GameGraphics
engine = GameGraphics()


class Button:
    def __init__(self, win, x1, y1, x2, y2, label):
        self.win = win
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.label = label

        self.rect = graphics.Rectangle(graphics.Point(x1, y1),
                                       graphics.Point(x2, y2))
        self.rect.setFill("gray20")
        self.rect.draw(win)

        self.text = graphics.Text(
            graphics.Point((x1 + x2)//2, (y1 + y2)//2),
            label
        )
        self.text.setSize(20)
        self.text.setFill("white")
        self.text.draw(win)

    def clicked(self, p):
        return (self.x1 <= p.getX() <= self.x2 and
                self.y1 <= p.getY() <= self.y2)

def show_home_screen(self):
    self.win.delete("all")
    self.messages.clear()

    title = graphics.Text(graphics.Point(self.width//2, 100), "Gin Rummy")
    title.setSize(36)
    title.setFill("white")
    title.draw(self.win)

    rules = graphics.Text(
        graphics.Point(self.width//2, 200),
        "Form melds. Reduce deadwood. Knock at 10 or less.\nFirst to 100 wins."
    )
    rules.setSize(18)
    rules.setFill("white")
    rules.draw(self.win)

    play_btn = Button(self.win, 200, 300, 450, 360, "Play Game")
    quit_btn = Button(self.win, 200, 380, 450, 440, "Quit")

    while True:
        click = self.win.getMouse()
        if play_btn.clicked(click):
            return "play"
        if quit_btn.clicked(click):
            return "quit"



def show_hand(label, hand):
    '''prints cards and their index number
    EX Your hand: [0:A♠] [1:7♥] [2:7♣]'''
    
    
    #switches to graphics
    engine.clear_messages()
    engine.show_message(label)
    engine.draw_hand(hand)

   
  

def show_top_of_discard(discard):
    '''prints the top card or says empty'''
    engine.clear_messages()
    engine.show_message("Top of Discard:", 100)

    if len(discard) == 0:
        engine.show_message("EMPTY", 140)
        return

    top = discard[-1]
    engine.draw_hand([top], y=200)

def ask_choice(prompt, options):
    '''shows options (Draw deck, Take discard, knock) and returns the chosen key'''

    engine.clear_messages()
    engine.show_message("Choose an action:", 30)

    b1 = engine.draw_button("Draw Deck", 200, 120)
    b2 = engine.draw_button("Take Discard", 450, 120)
    b3 = engine.draw_button("Knock", 700, 120)

    while True:
        p = engine.wait_for_click()
        x, y = p.getX(), p.getY()

        if inside_button(b1, x, y):
            return "1"
        if inside_button(b2, x, y):
            return "2"
        if inside_button(b3, x, y):
            return "3"

def inside_button(rect, x, y):
    p1 = rect.getP1()
    p2 = rect.getP2()
    return (p1.getX() <= x <= p2.getX()) and (p1.getY() <= y <= p2.getY())

def ask_index(prompt, limit):
    '''asks for a number and return it; this tells us which card to discard'''
    engine.show_message(prompt, 350)

    while True:
        click = engine.wait_for_click()
        cx, cy = click.getX(), click.getY()

        #card bounding box detection  
        spacing = 90
        x_start = (engine.width - spacing * (limit - 1)) // 2
        y = 450  # row where cards are drawn

        #cards are 80×120
        card_w = 80
        card_h = 120

        for i in range(limit):
            card_x = x_start + i * spacing

            if (card_x - card_w//2 <= cx <= card_x + card_w//2 and
                y - card_h//2 <= cy <= y + card_h//2):
                return i



