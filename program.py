import pygame
import random

from word import Word

# Define some colors
bg_color = (30, 30, 30)

# Set up the pygame window
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Codenames")

pygame.init()

# Initialize the font
font = pygame.font.Font(None, 36)

# Define the InputField class
class InputField:
    def __init__(self, font, color, pos, width, height):
        self.font = font
        self.color = color
        self.pos = pos
        self.width = width
        self.height = height
        self.rect = pygame.Rect(pos, (width, height))
        self.text = ""
        self.text_surface = self.font.render(self.text, True, self.color)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.text_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.text_surface, self.rect)


# Set up the grid
grid_rows = 5
grid_cols = 5
square_size = 140
square_spacing = 15

# Set up the scores
score_team_1 = 0
score_team_2 = 0

# Set up the input field
clue_input = InputField(font, (255, 255, 255), (780, 500), 500, 50)

# Set up the teams
current_team = 1
# Set up the list of words
words = [
    "Apple",
    "Banana",
    "Salt",
    "Bridge",
    "Samsung",
    "Arm",
    "Turkey",
    "Charge",
    "Moon",
    "Minute",
    "Church",
    "Staff",
    "Meth",
    "Plastic",
    "Net",
    "War",
    "Berlin",
    "Pants",
    "Makeup",
    "Joker",
    "America",
    "Scorpion",
    "Virus",
    "Oil",
    "Dream",
]

# Shuffle the words
random.shuffle(words)

# Create a list of lists to store the squares
squares = []
word_objects = []
for i in range(grid_rows):
    row = []
    for j in range(grid_cols):
        x = j * (square_size + square_spacing)
        y = i * (square_size + square_spacing)

        # Create the square and add it to the list
        square = pygame.Rect(x, y, square_size, square_size)
        row.append(square)

        # Make sure the index is within the bounds of the words list
        if i * grid_cols + j < len(words):
            # Create a Word object for this square
            word = Word(words[i * grid_cols + j])

            # Add the Word object to the list
            word_objects.append(word)
    squares.append(row)


running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the mouse is over a word
            for i in range(grid_rows):
                for j in range(grid_cols):
                    if i * grid_cols + j < len(word_objects):
                        # Get the square and word at this position in the grid
                        square = squares[i][j]
                        word = word_objects[i * grid_cols + j]
                    # Check if the mouse is over the square
                    if square.collidepoint(mouse_x, mouse_y):
                        # The mouse is over the square, so mark the word as guessed and update the score
                        word.guessed = True
                        if word.guessed:
                            if current_team == word.team:
                                # The team has picked the correct word, so award points
                                if current_team == 1:
                                    score_team_1 += 1
                                    current_team = 2
                                else:
                                    score_team_2 += 1
                                    current_team = 1
                            else:
                                # The team has picked the wrong word, so do not award points
                                pass

        else:
            # Pass the event to the input field
            clue_input.handle_event(event)

    # Draw the background
    screen.fill(bg_color)

    # Draw the squares
    for i in range(grid_rows):
        for j in range(grid_cols):
            # Make sure the index is within the bounds of the word_objects list
            if i * grid_cols + j < len(word_objects):
                # Get the square and word at this position in the grid
                square = squares[i][j]
                word = word_objects[i * grid_cols + j]

                # Draw the square
                pygame.draw.rect(screen, (235, 191, 140), square)

                # Draw the word
                word.draw(screen, font, square_size, square.x, square.y)

    # Render the scores
    score_team_1_text = font.render(f"Team 1: {score_team_1}", True, (255, 0, 0))
    score_team_2_text = font.render(f"Team 2: {score_team_2}", True, (255, 0, 0))

    # Calculate the size of the scores
    score_team_1_width, score_team_1_height = font.size(f"Team 1: {score_team_1}")
    score_team_2_width, score_team_2_height = font.size(f"Team 2: {score_team_2}")

    # Calculate the position of the scores
    score_team_1_x = 780
    score_team_1_y = 100
    score_team_2_x = 780
    score_team_2_y = 600

    # Draw the scores
    screen.blit(score_team_1_text, (score_team_1_x, score_team_1_y))
    screen.blit(score_team_2_text, (score_team_2_x, score_team_2_y))

    # Draw the input field
    clue_input.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
