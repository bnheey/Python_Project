import pygame

# pygame 을 import 하면 반드시 초기화를 해줘야한다.
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Myoung Game") # 게임 이름

# 이벤트 루프
running = True # 게임이 진행중인지 확인

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행되지 않음


# 게임이 종료되면 pygame도 종료
pygame.quit()