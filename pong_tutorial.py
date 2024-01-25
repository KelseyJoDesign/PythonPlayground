import pygame
import sys

# Initialize Pygame
pygame.init()
# Load Silkscreen font
silkscreen_font_path = r'C:\KelsCodes\YarnBall\Silkscreen-Regular.ttf'  # Update with the actual path
silkscreen_font = pygame.font.Font(silkscreen_font_path, 36)
 
# Screen dimensions
WIDTH, HEIGHT = 800, 600

#Set up Code----------------------------------------------------------------------------

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KelsCodes Yarn Ball")

# Colors
NAVY = (30, 30, 106)
WHITE = (255, 255, 255)
ORANGE = (229, 135, 85)
PURPLE = (156, 142, 188)

# Paddle properties
paddle_a = paddle_a_image = pygame.image.load('C:/KelsCodes/YarnBall/YarnBall_Assets-BearPaw.png')
paddle_b = paddle_b_image = pygame.image.load('C:/KelsCodes/YarnBall/YarnBall_Assets-ZoeyPaw.png')
PADDLE_WIDTH, PADDLE_HEIGHT = 160, 135
paddle_a_image = pygame.transform.scale(paddle_a_image, (PADDLE_WIDTH, PADDLE_HEIGHT))
paddle_b_image = pygame.transform.scale(paddle_b_image, (PADDLE_WIDTH, PADDLE_HEIGHT))
paddle_speed = 10

# Ball properties
ball_image = pygame.image.load('C:/KelsCodes/YarnBall/YarnBall_Assets-Ball.png')
BALL_SIZE = 50
ball_image = pygame.transform.scale(ball_image, (BALL_SIZE, BALL_SIZE))
ball_speed_x, ball_speed_y = 2, 2
MAX_BALL_SPEED_Y = 2.5

# Create paddles and ball
paddle_a = pygame.Rect(0, (HEIGHT - PADDLE_HEIGHT) / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(WIDTH - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH / 2 - BALL_SIZE / 2, HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE, BALL_SIZE)

# Score
bounce_count_a = 0
bounce_count_b = 0
high_score = 0
high_scorer_initials = ""

# Function to display the start screen with "GO!" button
def start_screen():
   # Load and scale images for Zoey and Bear
    bear_image = pygame.image.load('C:/KelsCodes/YarnBall/YarnBall_Assets-Bear.png')
    zoey_image = pygame.image.load('C:/KelsCodes/YarnBall/YarnBall_Assets_Zoey.png')
    BEAR_WIDTH, BEAR_HEIGHT = 160, 135
    ZOEY_WIDTH, ZOEY_HEIGHT = 160, 135
    bear_image = pygame.transform.scale(bear_image, (BEAR_WIDTH, BEAR_HEIGHT))
    zoey_image = pygame.transform.scale(zoey_image, (ZOEY_WIDTH, ZOEY_HEIGHT))

    # Rectangles for positioning Zoey and Bear
    bear_rect = pygame.Rect(0, (HEIGHT - BEAR_HEIGHT) / 2, BEAR_WIDTH, BEAR_HEIGHT)
    zoey_rect = pygame.Rect(WIDTH - ZOEY_WIDTH, (HEIGHT - ZOEY_HEIGHT) / 2, ZOEY_WIDTH, ZOEY_HEIGHT)

    # Load and scale the "GO!" button image
    go_button_image = pygame.image.load('C:/KelsCodes/YarnBall/YarnBall_Assets-GoBall.png')
    GO_WIDTH, GO_HEIGHT = 160, 135
    go_button_image = pygame.transform.scale(go_button_image, (GO_WIDTH, GO_HEIGHT))

    # Create a rect for the scaled image
    go_button_rect = go_button_image.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))

     # Start screen loop
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            # ... [event handling code] ...

            screen.fill(NAVY)
        
        # Draw Zoey and Bear
        screen.blit(bear_image, bear_rect.topleft)
        screen.blit(zoey_image, zoey_rect.topleft)

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if go_button_rect.collidepoint(mouse_pos):
                    waiting_for_input = False

        screen.fill(NAVY)
        # Draw the "GO!" button
        screen.blit(go_button_image, go_button_rect.topleft)
        pygame.display.flip()

# Call start_screen function before the game loop
start_screen()

# Game loop --------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= paddle_speed
    if keys[pygame.K_s] and paddle_a.bottom < HEIGHT:
        paddle_a.y += paddle_speed
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_b.bottom < HEIGHT:
        paddle_b.y += paddle_speed

    # Update ball position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

   # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

     # Ball collision with paddles
    if ball.colliderect(paddle_a):
        ball_speed_x *= -1
        bounce_count_a += 1

        # Adjust ball's vertical speed based on collision point
        impact_point = ball.centery - paddle_a.centery
        ball_speed_y = impact_point / (PADDLE_HEIGHT / 2) * MAX_BALL_SPEED_Y  # Adjust MAX_BALL_SPEED_Y as needed

    if ball.colliderect(paddle_b):
        ball_speed_x *= -1
        bounce_count_b += 1

        # Adjust ball's vertical speed based on collision point
        impact_point = ball.centery - paddle_b.centery
        ball_speed_y = impact_point / (PADDLE_HEIGHT / 2) * MAX_BALL_SPEED_Y  # Adjust MAX_BALL_SPEED_Y as needed
    
    # Ball out of bounds
    if ball.left <= 0:
        game_over = True
        ball = pygame.Rect(WIDTH / 2 - BALL_SIZE / 2, HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE, BALL_SIZE)
    elif ball.right >= WIDTH:
        game_over = True
        ball = pygame.Rect(WIDTH / 2 - BALL_SIZE / 2, HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE, BALL_SIZE)

    # Drawing
    screen.fill(NAVY)
    screen.blit(paddle_a_image, paddle_a.topleft)
    screen.blit(paddle_b_image, paddle_b.topleft)
    # Draw the ball
    screen.blit(ball_image, (ball.x, ball.y))
    score_text = font.render(f"Player A: {score_a} Player B: {score_b}", True, WHITE)
    screen.blit(score_text, (WIDTH / 2 - score_text.get_width() / 2, 20))

    # Function to get user initials
    def get_user_initials():
        initials = ""
        while len(initials) < 3:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha():
                        initials += event.unicode.upper()
                    elif event.key == pygame.K_BACKSPACE:
                        initials = initials[:-1]
                    elif event.key == pygame.K_RETURN and len(initials) == 3:
                        return initials
            screen.fill(NAVY)
            temp_text = font.render(f"Enter your initials: {initials}", True, WHITE)
            screen.blit(temp_text, (WIDTH / 2 - temp_text.get_width() / 2, HEIGHT / 2))
            pygame.display.flip()
        return initials

 # End of game and high score check
    # Replace this with your game-over logic
    if game_over:
        current_score = bounce_count_a + bounce_count_b
        if current_score > high_score:
            high_score = current_score
            high_scorer_initials = get_user_initials()

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
sys.exit()
