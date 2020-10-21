import pygame, random
from pygame.locals import *

# Randomização maçã
def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y //10 * 10)

# Colisão cobra maçã
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Inciando pygame e tela
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

# Criando cobra
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

# Criando maçã
apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

# Direção inicial
my_direction = LEFT

# Pontuação
score = 0

# Velocidade da cobra
speed = 15
clock = pygame.time.Clock()

while True:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        # Teclas de movimentação
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT
    
    # Cobra comendo maçã
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        score = score + 1
        speed = speed + 1
    
    # Colisão cobra com cantos da tela
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        pygame.quit()
        exit()
    # Colisão cobra com seu corpo
    for i in range(1,len(snake) -1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            pygame.quit()
            exit()

    # Direcionamento da cobra
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])


    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    
    
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)

    # Denhando delimitação da tela
    # Desenhando no eixo x
    #pygame.draw.line(screen, (0,255, 0), [0, 0], [50,30], 5)
    #for x in range(0, 600, 10):
        #pygame.draw.line(screen, (0, 255, 0), (x, 0), (x, 600))
    # Desenhando no eixo y
    #for y in range(0, 600, 10):
        #pygame.draw.line(screen, (0, 255, 0), (0, y), (600, y))

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()