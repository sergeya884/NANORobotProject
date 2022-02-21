import RPi.GPIO as GPIO
import time

# Pin Definitions
output_pin = 18  # BOARD pin 12, BCM pin 18

def go_forward():
	GPIO.output(motor_pin_r_b, LOW)
	GPIO.output(motor_pin_l_b, LOW)
	GPIO.output(motor_pin_r_f, HIGHT)
	GPIO.output(motor_pin_l_f, HIGHT)
def go_back():
	GPIO.output(motor_pin_r_f, LOW)	
	GPIO.output(motor_pin_l_f, LOW)
	GPIO.output(motor_pin_r_b, HIGHT)
	GPIO.output(motor_pin_l_b, HIGHT)
def turn_left():
	GPIO.output(motor_pin_r_f, LOW)
	GPIO.output(motor_pin_l_b, LOW)
	GPIO.output(motor_pin_r_f, HIGHT)
	GPIO.output(motor_pin_r_b, HIGHT)
def turn_right():
	GPIO.output(motor_pin_l_f, LOW)
	GPIO.output(motor_pin_l_b, LOW)
	GPIO.output(motor_pin_r_f, HIGHT)
	GPIO.output(motor_pin_r_b, HIGHT)
def stop():
	GPIO.output(motor_pin_l_f, LOW)
	GPIO.output(motor_pin_l_b, LOW)
	GPIO.output(motor_pin_r_f, LOW)
	GPIO.output(motor_pin_r_b, LOW)

GPIO.setup(motor_pin_l_f, GPIO.OUT)
GPIO.setup(motor_pin_l_b, GPIO.OUT)
GPIO.setup(motor_pin_r_f, GPIO.OUT)
GPIO.setup(motor_pin_r_b, GPIO.OUT)
GPIO.setup(motor_pin_r_b, GPIO.OUT)

def go_forward()
time.sleep(1)
stop()

GPIO.cleanup()
