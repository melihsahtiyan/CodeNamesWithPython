import pygame
import random

from word import Word

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GRID_ROWS = 5
GRID_COLS = 5
SQUARE_SIZE = 100
SQUARE_SPACE = 15
FONT_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Codenames")
pygame.mixer.music.load("brba.mp3")
pygame.mixer.music.play(-1)

# Set up the clock
clock = pygame.time.Clock()

# Load the font
font = pygame.font.Font(None, FONT_SIZE)

# List of words
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

# Shuffle the list of words
random.shuffle(words)

# Set up the grid
grid_rows = 5
grid_cols = 5
square_size = 100

# Create a list of squares
squares = [[None] * grid_cols for _ in range(grid_rows)]
for i in range(grid_rows):
    for j in range(grid_cols):
        x = j * SQUARE_SIZE
        y = i * SQUARE_SIZE
        squares[i][j] = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)

# Set up the teams
team_1_score = 0
team_2_score = 0
team_1 = (0, 0, 255)  # Blue
team_2 = (255, 0, 0)  # Red
current_team = team_1

# Initialize the word objects and squares
word_objects = []
squares = []
for i in range(grid_rows):
    row = []
    for j in range(grid_cols):
        # Choose a team for the word
        if (i * grid_cols + j) % 2 == 0:
            team = team_1
        else:
            team = team_2

        # Add the word to the list of word objects
        if (i * grid_cols + j) < len(words):
            word_objects.append(Word(words[i * grid_cols + j], team))

        # Add the square to the list of squares
        square = pygame.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        row.append(square)
    squares.append(row)


# Set up the input field
input_text = ""
input_rect = pygame.Rect(0, 0, 200, 50)
input_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

# Set up the game state
game_over = False

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # Check if a square was clicked
            for i in range(grid_rows):
                for j in range(grid_cols):
                    square = squares[i][j]
                    if square.collidepoint(event.pos):
                        word = word_objects[i * grid_cols + j]
                        if word.guessed:
                            continue
                        word.guessed = True
                        if word.team == current_team:
                            if current_team == team_1:
                                team_1_score += 1
                            else:
                                team_2_score += 1
                        else:
                            if current_team == team_1:
                                current_team = team_2
                            else:
                                current_team = team_1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                # Check if the input is a valid word
                for word in word_objects:
                    if word.text == input_text and not word.guessed:
                        word.guessed = True
                        if word.team == current_team:
                            if current_team == team_1:
                                team_1_score += 1
                            else:
                                team_2_score += 1
                        else:
                            if current_team == team_1:
                                current_team = team_2
                            else:
                                current_team = team_1
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Draw the background
    screen.fill(BLACK)

    # Draw the squares and words
    for i in range(grid_rows):
        for j in range(grid_cols):
            x = j * SQUARE_SIZE
            y = i * SQUARE_SIZE
            square = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, (235, 191, 140), square)
            if (i * grid_cols + j) < len(word_objects):
                word = word_objects[i * grid_cols + j]
                if word.team == team_1:
                    color = team_1
                else:
                    color = team_2
                word.draw(screen, font, x, y, SQUARE_SIZE)

    # Draw the input field
    pygame.draw.rect(screen, WHITE, input_rect)
    input_surface = font.render(input_text, True, BLACK)
    input_rect = input_surface.get_rect()
    input_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
    screen.blit(input_surface, input_rect)

    # Draw the team scores
    team_1_surface = font.render(f"Team 1: {team_1_score}", True, team_1)
    team_1_rect = team_1_surface.get_rect()
    team_1_rect.left = 10
    team_1_rect.top = 10
    screen.blit(team_1_surface, team_1_rect)

    team_2_surface = font.render(f"Team 2: {team_2_score}", True, team_2)
    team_2_rect = team_2_surface.get_rect()
    team_2_rect.right = SCREEN_WIDTH - 10
    team_2_rect.top = 10
    screen.blit(team_2_surface, team_2_rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
