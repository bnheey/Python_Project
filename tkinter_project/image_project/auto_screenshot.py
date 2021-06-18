import time
from PIL import ImageGrab

# 사용자의 준비시간을 위하여 시작 후 5초 대기한다.
time.sleep(5)

# 2초 간격으로 이미지 10장을 추출한다.
for i in range(1, 11):
    img = ImageGrab.grab() # 현재 스크린의 이미지를 가져옴
    img.save("image{}.png".format(i)) # 파일로 저장 (image1.png ~ image10.png)
    time.sleep(2)