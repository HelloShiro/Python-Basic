# Snake Game!!

import pygame, sys, random, time

check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} initailing errors, exiting...", format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized")

# Play Surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game!!')

# Colors(r,g,b)
red = pygame.Color(255, 0, 0)  # gameover
green = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(162, 42, 42)  # food

# FPS (frame per second) controller

fpsController = pygame.time.Clock()

# Important Varibles
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50], [50, 50], [40, 50], [30, 50], [20, 50], [10, 50]]
foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score = 0


# Game over func
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    Gosurf = myFont.render('Game over!', True, red)
    Gorect = Gosurf.get_rect()
    Gorect.midtop = (360, 15)
    playSurface.blit(Gosurf, Gorect)
    pygame.display.flip()
    showScore(0)
    time.sleep(1.5)
    pygame.quit()  # pygame
    sys.exit()  # console


def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 50)
    Ssurf = sFont.render('Score: {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playSurface.blit(Ssurf, Srect)



# Main Logic of the Game


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    # Update snake position[x,y]
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
    # Sanke body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False

    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    # Draw Snake
    playSurface.fill(white)
    for i in range(0, len(snakeBody)):
        pygame.draw.rect(playSurface, black, pygame.Rect(snakeBody[i][0], snakeBody[i][1], 10, 10))
    ##
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()

    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()
    for body in snakeBody[1:]:
        if snakePos[0] == body[0] and snakePos[1] == body[1]:
            gameOver()

    showScore()
    pygame.display.flip()
    fpsController.tick(20)
