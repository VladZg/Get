import RPi.GPIO as GPIO
import time

def bin_translator(num, delay):
    number = [0 for i in range(8)]
    d_num = num % 256
    bin_num = bin(d_num)

    i = -1
    while bin_num[i] != 'b':
        number[i] = int(bin_num[i])
        i -= 1

    print("{} --> {}".format(num, number))

    GPIO.output(dac, number)
    volt = float(input())
    voltage.append(volt)
    # time.sleep(delay)

    return 0

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
voltage = []

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

# for i in range (0, 256):
    # bin_translator(i, 0.2)

nums = [0, 5, 32, 64, 127, 255, 256]

for i in nums:
    bin_translator(i, 10)   

print(voltage)  # output: [-0.485, -0.485, -0.5, -0.825, -1.626, -3.249, -0.485] 

GPIO.output(dac, 0)
GPIO.cleanup()