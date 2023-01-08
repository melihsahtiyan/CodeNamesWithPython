import pygame


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

    def draw(self, screen):
        # Draw the input field
        pygame.draw.rect(screen, self.color, self.rect)

        # Render the text as a surface and blit it onto the screen
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, self.pos)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            # Check if the key is a printable character
            if event.unicode.isprintable():
                # Add the character to the text
                self.text += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                # Remove the last character from the text
                self.text = self.text[:-1]
