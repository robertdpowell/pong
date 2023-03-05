import pygame, sys
import random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        ball_restart()
        player_score += 1

    if ball.right >= screen_width:
        ball_restart()
        opponent_score += 1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

pygame.init()
clock = pygame.time.Clock()

#setting up main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')


#game rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width -20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70,10,140)

bg_colour = pygame.Color('grey12')
light_grey = (200,200,200)
player_colour = (204, 0, 204)
opponent_colour = (102, 255, 255)
ball_colour = (255, 255, 153)

#track speeds
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 0

#tracking scores
player_score = 0
opponent_score = 0

# set up font for rendering scores
font = pygame.font.SysFont(None, 48)

while True:
    #handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 10
            if event.key ==pygame.K_UP:
                player_speed -= 10

            if event.key == pygame.K_a:
                opponent_speed += 10
            if event.key == pygame.K_q:
                opponent_speed -= 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 10
            if event.key == pygame.K_UP:
                player_speed += 10

            if event.key == pygame.K_a:
                opponent_speed -= 10
            if event.key == pygame.K_q:
                opponent_speed += 10

    ball_animation()
    player_animation()
    opponent_animation()

    #visuals
    screen.fill(bg_colour)
    pygame.draw.rect(screen, player_colour, player)
    pygame.draw.rect(screen, opponent_colour, opponent)
    pygame.draw.ellipse(screen, ball_colour, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))

    # render scores as text
    player_score_text = font.render(str(player_score), True, light_grey)
    opponent_score_text = font.render(str(opponent_score), True, light_grey)
    screen.blit(player_score_text, (screen_width / 2 + 16, 16))
    screen.blit(opponent_score_text, (screen_width / 2 - 48, 16))


    pygame.display.flip()
    clock.tick(60)

