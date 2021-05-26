'''
오락실 pang 게임 만들기

[게임 조건]
1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
2. 스페이스를 누르면 무기를 쏘아 올림
3. 큰 공 1개가 나타나서 바운스
4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
5. 모든 공을 없애면 게임 종료(성공)
6. 캐릭터는 공에 닿으면 게임 종료(실패)
7. 시간 제한 99초 초과시 게임 종료(실패)
8. FPS는 30으로 고정(필요시 speed 값을 조정)

[게임 이미지]
1. 배경 : 640 * 480(가로, 세로) - background.png
2. 무대 : 640 * 50 - stage.png
3. 캐릭터 : 33 * 60 - character.png
4. 무기 : 20 * 43 weapon.png
5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20 - ball1.png ~ ball4/png
'''
import os

import pygame

# 기본 초기화(반드시 해야하는 것들)
# pygame 을 import 하면 반드시 초기화를 해줘야한다.
pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("SPLIT BALLOON GAME")

# 이동할 좌표
to_x = 0
# 이동 속도
character_speed = 0.6

# FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "background.png"))

stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]
stage_y_pos = screen_height - stage_height

character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height - stage_height

weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

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
            elif event.key == pygame.K_SPACE:
                # 무기 위치 정의
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt
    # 3. 게임 캐릭터 위치 정의
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = screen_width - character_width

    # 무기 이동 조절
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # 4. 충돌 처리

    # 5. 화면에 그리기 - screen.blit
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, stage_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))

    for weapon_x_pos, weapon_y_pos in weapons :
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))



    pygame.display.update()

pygame.quit()
