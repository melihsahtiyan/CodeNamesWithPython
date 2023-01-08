class Word:
    def __init__(self, word):
        self.word = word
        self.guessed = False

    def draw(self, screen, font, square_size, square_x, square_y):
        # Render the text
        text = font.render(self.word, True, (30, 30, 30))

        # Calculate the size of the text
        text_width, text_height = font.size(self.word)

        # Calculate the position of the text
        text_x = square_x + (square_size - text_width) // 2
        text_y = square_y + (square_size - text_height) // 2

        # Draw the text
        screen.blit(text, (text_x, text_y))
