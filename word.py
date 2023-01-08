class Word:
    def __init__(self, word, team):
        self.word = word
        self.team = team
        self.guessed = False

    def draw(self, screen, font, x, y, square_size):
        # Render the word as an image
        word_image = font.render(self.word, True, (30, 30, 30))
        word_rect = word_image.get_rect()
        word_rect.center = (x + square_size / 2, y + square_size / 2)
        screen.blit(word_image, word_rect)
