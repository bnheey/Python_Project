import pygame

# pygame 을 import 하면 반드시 초기화를 해줘야한다.
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Myoung Game")  # 게임 이름

# 배경이미지 불러오기
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
to_y = 0

# 이벤트 루프
running = True  # 게임이 진행중인지 확인

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행되지 않음

        if event.type == pygame.KEYDOWN:  # 키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT:  # 왼쪽 키 눌림
                to_x -= 5
            elif event.key == pygame.K_RIGHT:  # 오른쪽 키 눌림
                to_x += 5
            elif event.key == pygame.K_UP:  # 위쪽 키 눌림
                to_y -= 5
            elif event.key == pygame.K_DOWN:  # 아래쪽 키 눌림
                to_y += 5

        if event.type == pygame.KEYUP:  # 방향키 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    # 게임 화면을 다시 그리기! background가 계속 프레임에 뜨게 하기 위해서!
    pygame.display.update()

# 게임이 종료되면 pygame도 종료
pygame.quit()
