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
    def show_home_screen(self):
        self.win.delete("all")
        self.messages.clear()
        self.drawn_cards.clear()
        self.discard_image = None
        self.win.setBackground(TABLE_COLOR)

    # Title
        title = graphics.Text(graphics.Point(self.width//2, 80), "Gin Rummy")
        title.setSize(36)
        title.setFill("white")
        title.draw(self.win)

    # Rules text
        rules_text = (
            "Basic Rules:\n"
            "• You start with 10 cards.\n"
            "• On your turn, draw from deck or discard.\n"
            "• Discard 1 card at the end of your turn.\n"
            "• Create melds (3+ in a run or set).\n"
            "• Knock when your deadwood ≤ 10.\n"
            "• Lowest deadwood wins unless undercut."
        )

        rules = graphics.Text(graphics.Point(self.width//2, 230), rules_text)
        rules.setSize(18)
        rules.setFill("white")
        rules.draw(self.win)

    # Play button
        play_btn = graphics.Rectangle(
            graphics.Point(325, 350),
            graphics.Point(625, 420)
        )
        play_btn.setFill("white")
        play_btn.draw(self.win)

        play_label = graphics.Text(graphics.Point(475, 385), "Play Game")
        play_label.setSize(20)
        play_label.draw(self.win)

    # Quit button
        quit_btn = graphics.Rectangle(
            graphics.Point(325, 450),
            graphics.Point(625, 520)
        )
        quit_btn.setFill("white")
        quit_btn.draw(self.win)

        quit_label = graphics.Text(graphics.Point(475, 485), "Quit")
        quit_label.setSize(20)
        quit_label.draw(self.win)

    # Event loop
        while True:
            click = self.win.getMouse()
            x, y = click.getX(), click.getY()

            if 250 <= x <= 550 and 350 <= y <= 420:
            # Remove everything
                self.win.delete("all")
                return "play"

            if 250 <= x <= 550 and 450 <= y <= 520:
                self.win.close()
                return "quit"
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
        width = 180
        height = 50

        box = graphics.Rectangle(
            graphics.Point(x - width//2, y - height//2),
            graphics.Point(x + width//2, y + height//2)
        )
        box.setFill("gray30")
        box.draw(self.win)

        text = graphics.Text(graphics.Point(x, y), label)
        text.setSize(20)
        text.setFill("white")
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