import graphics
from SetUp import card_to_file

CARD_WIDTH = 80
CARD_HEIGHT = 120
TABLE_COLOR = "darkgreen"

class GameGraphics:
    def __init__(self, width=900, height=600):
        self.win = graphics.GraphWin("Gin Rummy", width, height)
        self.win.setBackground(TABLE_COLOR)
        self.width = width
        self.height = height
        self.messages = []
        self.drawn_cards = []

#shows the text on screen
    def clear_messages(self):
        for m in self.messages:
            m.undraw()
        self.messages = []

    def show_message(self, text, y_offset=30):
        msg = graphics.Text(graphics.Point(self.width//2, y_offset), text)
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

    def wait_for_click(self):
        return self.win.getMouse()

    def close(self):
        self.win.close()