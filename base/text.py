from base.sprite import Sprite


class Text(Sprite):
    text = None
    text_color = None

    pos = None
    font = None

    def __init__(self, pos, font, text, text_color):
        super().__init__({}, {})
        self.pos = pos
        self.text_color = text_color
        self.text = text
        self.font = font
        self.update_text()

    # TEXT ALWAYS SHOULD BE UPDATED AFTER CHANGING IT
    def update_text(self):
        self.surfaces["main"] = self.font.render(self.text, False, self.text_color)
        self.rects["main"] = self.surfaces["main"].get_rect(topleft=self.pos)
