import pygame

# pygame 을 import 하면 반드시 초기화를 해줘야한다.
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Myoung Game") # 게임 이름

# 배경이미지 불러오기
background = pygame.image.load("/pygame_project/pygame_basic/images/background.png")

# 이벤트 루프
running = True # 게임이 진행중인지 확인

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행되지 않음

    screen.blit(background, (0, 0)) # 배경 그리기
    
    # 게임 화면을 다시 그리기! background가 계속 프레임에 뜨게 하기 위해서!
    pygame.display.update()


# 게임이 종료되면 pygame도 종료
pygame.quit()