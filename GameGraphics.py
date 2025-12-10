'''Graphics'''
import graphics
from SetUp import card_to_file

CARD_WIDTH = 80
CARD_HEIGHT = 120
TABLE_COLOR = "darkgreen"

class GameGraphics:
    def __init__(self, width=950, height=700):
        self.win = graphics.GraphWin("Gin Rummy", width, height)
        self.win.setBackground(TABLE_COLOR)
        self.width = width
        self.height = height
        self.messages = []
        self.drawn_cards = []
        self.discard_image = None

#shows the text on screen
    def clear_messages(self):
        for m in self.messages:
            m.undraw()
        self.messages = []

    def show_message(self, text, pos=30):
    # If pos is a tuple, treat it as (x, y)
        if isinstance(pos, tuple):
            x, y = pos
        else:
            # keep old behavior (centered horizontally, custom Y)
            x = self.width // 2
            y = pos

        msg = graphics.Text(graphics.Point(x, y), text)
        msg.setSize(18)
        msg.setFill("white")
        msg.draw(self.win)
        self.messages.append(msg)

#draws the cards
    def clear_cards(self):
        for c in self.drawn_cards:
            c.undraw()
        self.drawn_cards = []

    def draw_hand(self, cards, y=450, spacing=90):
        x = (self.width - spacing * (len(cards) - 1)) // 2

        for i, card in enumerate(cards):
            filename = card_to_file(card)
            img = graphics.Image(graphics.Point(x + i*spacing, y), f"cards/PNG-cards-1.3/{filename}")
            img.draw(self.win)
            self.drawn_cards.append(img)
            
#creates and uses buttons
    def draw_button(self, label, x, y):
        box = graphics.Rectangle(graphics.Point(x-60, y-20), graphics.Point(x+60, y+20))
        box.setFill("lightgray")
        box.draw(self.win)

        text = graphics.Text(graphics.Point(x, y), label)
        text.setSize(14)
        text.draw(self.win)

        return box
    
    def show_drawn_card(self, card):
        self.clear_messages()
        self.show_message("You drew:", (200, 75))
        img = graphics.Image(graphics.Point(self.width//5, 200),
                             f"cards/PNG-cards-1.3/{card_to_file(card)}")
        img.draw(self.win)
        self.drawn_cards.append(img)
        
    def draw_discard(self, card): 
        """Draw exactly one discard pile card."""
        # Remove previous discard card
        if self.discard_image:
            self.discard_image.undraw()

        filename = card_to_file(card)
        img = graphics.Image(
            graphics.Point(self.width//2, 150),  
            f"cards/PNG-cards-1.3/{filename}"
        )
        img.draw(self.win)
        self.discard_image = img
    

    def wait_for_click(self):
        return self.win.getMouse()

    def close(self):
        self.win.close()