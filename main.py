import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 100
target_height = 100

# Начальные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = (245, 245, 245)

# Счетчик нажатий
count = 0

# Скорость движения мишени
target_speed_x = 2
target_speed_y = 2

running = True

while running:
    screen.fill(color)
    time.sleep(0.01)

    # Движение мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка на столкновение с границами экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x  # Изменить направление по X
        target_x = max(0, min(target_x, SCREEN_WIDTH - target_width))  # Корректировка X

    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y  # Изменить направление по Y
        target_y = max(0, min(target_y, SCREEN_HEIGHT - target_height))  # Корректировка Y

    # Отрисовка мишени
    screen.blit(target_img, (target_x, target_y))

    # Отрисовка счетчика нажатий
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Нажатий: {count}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                count += 1

    pygame.display.update()

pygame.quit()
