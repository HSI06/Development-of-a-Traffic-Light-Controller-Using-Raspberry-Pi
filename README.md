# Raspberry Pi Traffic Light Controller

라즈베리파이를 활용하여 차량용 및 보행자용 신호등을 제어하는 프로젝트입니다.
GPIO 핀을 이용하여 LED를 제어하고, Python을 통해 신호 주기를 자동으로 관리합니다.

# Project Overview

이 프로젝트는 라즈베리파이의 GPIO 기능을 활용하여
3색 신호등(차량)과 2색 신호등(보행자)을 구현하는 것을 목표로 합니다.

차량 신호와 보행자 신호가 서로 연동되어
실제 교차로와 유사한 동작을 수행합니다.

# Theoretical Background
🔹 LED 동작 원리

LED는 전기에너지를 빛에너지로 변환하는 반도체 소자입니다.
긴 다리(Anode, +)와 짧은 다리(Cathode, -)의 극성이 있으며, 올바르게 연결해야 점등됩니다.

🔹 저항(330Ω) 사용 이유

LED는 과도한 전류가 흐르면 손상될 수 있습니다.
330Ω 저항을 사용하여 전류를 제한함으로써 LED와 GPIO 핀을 보호합니다.

# Tech Stack
Language: Python 3 

Library: gpiozero 

Hardware: Raspberry Pi 


# Hardware Configuration

| 역할 | GPIO 핀 |
|------|--------|
| 차량 빨강 | GPIO 2 |
| 차량 노랑 | GPIO 3 |
| 차량 초록 | GPIO 4 |
| 보행자 빨강 | GPIO 20 |
| 보행자 초록 | GPIO 21 |


# Traffic Light Logic
차량 초록 / 보행자 빨강 → 3초
차량 노랑 / 보행자 빨강 → 1초
차량 빨강 / 보행자 초록 → 3초

위 과정을 반복하여 신호등을 제어합니다.

# How to Run
python main2.py


# Demo Video

https://www.youtube.com/shorts/z3oX7vqhkjI

# Description

본 프로젝트는 라즈베리파이의 GPIO 제어를 통해
하드웨어와 소프트웨어의 연동을 학습하는 데 목적이 있습니다.

LED 제어를 통해 신호등의 동작 원리를 이해하고,
시간 제어 로직을 활용하여 실제 시스템과 유사한 동작을 구현하였습니다.
