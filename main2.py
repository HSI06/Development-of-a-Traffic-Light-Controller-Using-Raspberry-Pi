# ==========================================================
# 과제명: 라즈베리파이로 신호등 만들기
# 학번: [202578207]
# 이름: [황사익]
# ----------------------------------------------------------
# [이론 설명]
# 1. LED 동작 원리: 
#    - 반도체 소자로, 순방향 전압을 걸어주면 전기에너지가 빛으로 변환됨.
#    - 긴 다리(Anode, +)와 짧은 다리(Cathode, -)의 극성을 맞춰야 함.
# 2. 저항(330Ω) 사용 이유: 
#    - LED는 과전류에 약해 직접 연결 시 파손될 위험이 있음.
#    - 저항을 통해 전류를 제한하여 LED와 라즈베리파이 GPIO 핀을 보호함.
# ==========================================================

from gpiozero import LED
from time import sleep

# [하드웨어 설정] 각 신호등 LED가 연결된 GPIO 핀 번호 할당
# 차량용 신호등 (Red: 2, Yellow: 3, Green: 4)
carLedRed = LED(2)
carLedYellow = LED(3)
carLedGreen = LED(4)

# 보행자용 신호등 (Red: 20, Green: 21)
humanLedRed = LED(20)
humanLedGreen = LED(21)

try:
    print("신호등 시스템을 시작합니다. 종료하려면 Ctrl+C를 누르세요.")
    
    while True:
        # [1단계] 차량: 초록불(GO) / 보행자: 빨간불(STOP)
        carLedRed.value = 0
        carLedYellow.value = 0
        carLedGreen.value = 1
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(3.0)  # 3초 유지

        # [2단계] 차량: 노란불(CAUTION) / 보행자: 빨간불(STOP)
        carLedRed.value = 0
        carLedYellow.value = 1
        carLedGreen.value = 0
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(1.0)  # 1초 유지

        # [3단계] 차량: 빨간불(STOP) / 보행자: 초록불(GO)
        carLedRed.value = 1
        carLedYellow.value = 0
        carLedGreen.value = 0
        humanLedRed.value = 0
        humanLedGreen.value = 1
        sleep(3.0)  # 3초 유지

except KeyboardInterrupt:
    # 사용자가 Ctrl+C를 눌러 프로그램을 중단했을 때 실행됨
    print("\n프로그램을 안전하게 종료합니다.")

finally:
    # [정리] 프로그램 종료 시 모든 LED를 꺼서 전기 소모를 방지함
    carLedRed.value = 0
    carLedYellow.value = 0
    carLedGreen.value = 0
    humanLedRed.value = 0
    humanLedGreen.value = 0