'''
하늘에서 떨어지는 똥 피하기 게임

[게임 조건]
1. 캐릭터은 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐. x좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS는 30으로 고정

[게임 이미지]
1. 배경 : 640* 480(세로, 가로) - background.png
2. 캐릭터 : 70 * 70 - character.png
3. 똥 : 70 * 70 enemy.png
'''
import random

import pygame

# 기본 초기화(반드시 해야하는 것들)
# pygame 을 import 하면 반드시 초기화를 해줘야한다.
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("ddong_avoid_game")

# 폰트 설정
game_font = pygame.font.Font(None, 40)

# 시간 설정
now = 0

# FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("images/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("images/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로크기
character_height = character_size[1]  # 캐릭터의 세로크기
character_x_pos = screen_width / 2 - character_width / 2  # 화면 가로 크기의 절반(가로 축 중앙에 배치)
character_y_pos = screen_height - character_height  # 화면 크기 가장 아래의 위치

# 이동할 좌표
to_x = 0
# 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("images/enemy.png")
enemy_size = character.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = character_size[0]  # 캐릭터의 가로크기
enemy_height = character_size[1]  # 캐릭터의 세로크기
enemy_x_pos = random.randint(0, screen_width - enemy_width)  # 화면 가로 크기의 절반(가로 축 중앙에 배치)
enemy_y_pos = 0  # 화면 크기 가장 아래의 위치
enemy_speed = 10

running = True

while running:
    dt = clock.tick(30)  # 게임화면의 초당 프레임 수

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행되지 않음

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:  # 방향키 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > (screen_width - character_width):
        character_x_pos = screen_width - character_width


    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height :
        enemy_y_pos = 0
        enemy_x_pos= random.randint(0, screen_width - enemy_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌!!")
        running = False


    # 5. 화면에 그리기 - screen.blit
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기


    elapsed_time = (pygame.time.get_ticks()) / 1000
    timer = game_font.render(str(int(elapsed_time)), True, (0, 0, 0))
    screen.blit(timer, (10, 10))
    pygame.display.update()

pygame.time.delay(1000)

pygame.quit()
