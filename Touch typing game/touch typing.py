import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
RED = (255, 0, 0)
FONT = pygame.font.Font(None, 36)

# Text to type (with a full stop)
text_to_type = "The quick brown fox jumps over the lazy dog."
word_list = text_to_type.split()
current_word = ""
correct_words = 0
total_words = len(word_list)
start_time = None
text_completed = False
typed_chars = 0  # Counter for typed characters
wpm = 0  # Words per minute

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Touch Typing Test")

def draw_text(text, x, y, color):
    rendered_text = FONT.render(text, True, color)
    screen.blit(rendered_text, (x, y))

def calculate_wpm(typed_chars, elapsed_time):
    if elapsed_time > 0:
        wpm = (typed_chars / 5) / (elapsed_time / 60)
        return wpm
    else:
        return 0

def main():
    global current_word, correct_words, start_time, text_completed, typed_chars, wpm
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not text_completed:
                typed_char = event.unicode

                if start_time is None:
                    start_time = time.time()

                if event.key == pygame.K_SPACE:
                    current_word += " "  # Add a space on spacebar press
                elif event.key == pygame.K_RETURN:
                    if current_word.strip() == word_list[correct_words]:
                        correct_words += 1
                        typed_chars += len(current_word) + 1  # Count spaces
                        current_word = ""

                        if correct_words == total_words:
                            text_completed = True  # Text completion flag
                    else:
                        current_word += " "  # Add a space on incorrect Enter press

                elif event.key == pygame.K_BACKSPACE:
                    current_word = current_word[:-1]  # Remove the last character on backspace
                else:
                    current_word += typed_char
                    typed_chars += 1

        screen.fill(WHITE)
        draw_text("Type the text below:", 20, 20, BLACK)
        
        # Display the current word typed with incorrect characters in red
        typed_text = text_to_type[:len(current_word)]
        untyped_text = text_to_type[len(current_word):]
        
        for i in range(len(current_word)):
            if current_word[i] != text_to_type[i]:
                draw_text(current_word[i], 20 + i * 14, 70, RED)
            else:
                draw_text(current_word[i], 20 + i * 14, 70, BLACK)
        
        draw_text(untyped_text, 20 + len(typed_text) * 14, 70, GRAY)
        
        if text_completed:
            elapsed_time = time.time() - start_time
            wpm = calculate_wpm(typed_chars, elapsed_time)

            result_text = f"Text completed!"
            result_text += f"\nWords per minute: {wpm:.2f} WPM"
            
            # Display results when Enter is pressed after text completion
            draw_text(result_text, 20, 200, BLACK)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
