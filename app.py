import pygame
from sys import exit

# Boilerplate
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("PONG")
clock = pygame.time.Clock()


def get_digit(number, n):
    return number // 10 ** n % 10


background_surface = pygame.Surface((800, 500)).convert()
background_surface.fill("Black")
paddle_surface = pygame.Surface((10, 50)).convert()
paddle_surface.fill("White")
ball_surface = pygame.Surface((10, 10)).convert()
ball_surface.fill("White")
line_surface = pygame.Surface((10, 500)).convert()
line_surface.fill("White")
P1score1_surface = pygame.image.load('Graphics/0.png').convert()
P1score2_surface = pygame.image.load('Graphics/0.png').convert()
P2score1_surface = pygame.image.load('Graphics/0.png').convert()
P2score2_surface = pygame.image.load('Graphics/0.png').convert()

# Variables
player1_score = 0
player2_score = 0

paddle1_pos = 225
paddle1_velocity = 0
paddle1_up = False
paddle1_down = False
paddle1_attack = 0

paddle2_pos = 225
paddle2_velocity = 0
paddle2_up = False
paddle2_down = False
paddle2_attack = 0

ball_x_pos = 195
ball_y_pos = 245
ball_x_velocity = 5
ball_y_velocity = 0

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_up = True
            if event.key == pygame.K_s:
                paddle1_down = True
            if event.key == pygame.K_UP:
                paddle2_up = True
            if event.key == pygame.K_DOWN:
                paddle2_down = True

        # Not Pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                paddle1_up = False
            if event.key == pygame.K_s:
                paddle1_down = False
            if event.key == pygame.K_UP:
                paddle2_up = False
            if event.key == pygame.K_DOWN:
                paddle2_down = False

    # Paddle 1 Movement
    paddle1_velocity = 0
    if paddle1_up is True and paddle1_down is False and paddle1_pos >= 0:
        paddle1_velocity = -5
    if paddle1_up is False and paddle1_down is True and paddle1_pos <= 450:
        paddle1_velocity = 5
    if paddle1_up is True and paddle1_down is True:
        paddle1_velocity = 0
    if paddle1_up is False and paddle1_down is False:
        paddle1_velocity = 0
    paddle1_pos = paddle1_pos + paddle1_velocity / 2

    # Paddle 2 Movement
    paddle2_velocity = 0
    if paddle2_up is True and paddle2_down is False and paddle2_pos >= 0:
        paddle2_velocity = -5
    if paddle2_up is False and paddle2_down is True and paddle2_pos <= 450:
        paddle2_velocity = 5
    if paddle2_up is True and paddle2_down is True:
        paddle2_velocity = 0
    if paddle2_up is False and paddle2_down is False:
        paddle2_velocity = 0
    paddle2_pos = paddle2_pos + paddle2_velocity / 2

    #Ball Movement on Paddle 1
    if 15 >= ball_x_pos >= 5 and ball_x_velocity == -5:
        if paddle1_pos + 50 >= ball_y_pos >= paddle1_pos - 10:
            ball_x_velocity = ball_x_velocity * -1
            paddle1_attack = ((ball_y_pos + 5) - (paddle1_pos + 25)) / 5
            ball_y_velocity = ball_y_velocity + paddle1_attack
    if ball_x_pos == -10:
        # Player 1 Wins
        ball_x_pos = 595
        ball_y_pos = 245
        ball_y_velocity = 0
        ball_x_velocity = -5
        player2_score = player2_score + 1
        P2score1_surface = pygame.image.load('Graphics/' + str(get_digit(player2_score, 1)) + '.png').convert()
        P2score2_surface = pygame.image.load('Graphics/' + str(get_digit(player2_score, 0)) + '.png').convert()

    # Ball Movement on Paddle 2
    if 775 <= ball_x_pos <= 785 and ball_x_velocity == 5:
        if paddle2_pos + 50 >= ball_y_pos >= paddle2_pos - 10:
            ball_x_velocity = ball_x_velocity * -1
            paddle2_attack = ((ball_y_pos + 5) - (paddle2_pos + 25)) / 5
            ball_y_velocity = ball_y_velocity + paddle2_attack
    if ball_x_pos == 800:
        # Player 1 wins
        ball_x_pos = 195
        ball_y_pos = 245
        ball_y_velocity = 0
        ball_x_velocity = 5
        player1_score = player1_score + 1
        P1score1_surface = pygame.image.load('Graphics/' + str(get_digit(player1_score, 1)) + '.png').convert()
        P1score2_surface = pygame.image.load('Graphics/' + str(get_digit(player1_score, 0)) + '.png').convert()

        # Y Bounce
    if not 0 < ball_y_pos < 490:
        ball_y_velocity = ball_y_velocity * -1
        # Y Velocity Limit
    if ball_y_velocity > 5:
        ball_y_velocity = 5
    if ball_y_velocity < -5:
        ball_y_velocity = -5

    ball_x_pos = ball_x_pos + ball_x_velocity / 2
    ball_y_pos = ball_y_pos + ball_y_velocity / 2

    # Rendering
    screen.blit(background_surface, (0, 0))
    screen.blit(line_surface, (395, 0))
    # score
    screen.blit(P1score1_surface, (315, 10))
    screen.blit(P1score2_surface, (355, 10))
    screen.blit(P2score1_surface, (415, 10))
    screen.blit(P2score2_surface, (455, 10))
    # other
    screen.blit(paddle_surface, (5, paddle1_pos))
    screen.blit(paddle_surface, (785, paddle2_pos))
    screen.blit(ball_surface, (ball_x_pos, ball_y_pos))
    # Other Rendering + Clock
    pygame.display.update()
    clock.tick(120)
