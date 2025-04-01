import RPi.GPIO as GPIO
import time

# 핀 설정
TRIG = 12       # 초음파 송신부
ECHO = 16       # 초음파 수신부
LED1 = 11       # LED1
LED2 = 13       # LED2
LED3 = 15       # LED3

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

try:
    while True:
        # 초음파
        GPIO.output(TRIG, False)
        time.sleep(0.5)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            start = time.time()

        while GPIO.input(ECHO) == 1:
            stop = time.time()

        time_interval = stop - start
        distance = time_interval * 17000
        distance = round(distance, 2)

        print(f"Distance : {distance} cm")
   
        # LED 제어
        if distance <= 10:
            GPIO.output(LED1, True)
            GPIO.output(LED2, False)
            GPIO.output(LED3, False)
        elif distance <= 20:
            GPIO.output(LED1, True)
            GPIO.output(LED2, True)
            GPIO.output(LED3, False)
        elif distance <= 30:
            GPIO.output(LED1, True)
            GPIO.output(LED2, True)
            GPIO.output(LED3, True)
        else:
            GPIO.output(LED1, True)
            GPIO.output(LED2, True)
            GPIO.output(LED3, True)

except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    GPIO.cleanup()
