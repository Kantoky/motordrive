# coding: utf-8
import RPi.GPIO as GPIO
import time
import wiringpi as wp

class Drive:
    MaxdutyRange = 1024
    #default io 5/6/7/8 , PWM 12/13
    def __init__(self, PIN_IN1_L=5, PIN_IN2_L=6, PIN_IN1_R=7, PIN_IN2_R=8, PIN_VREF_L=12, PIN_VREF_R=13):
        self.PIN_IN1_L = PIN_IN1_L
        self.PIN_IN1_R = PIN_IN1_R
        self.PIN_IN2_L = PIN_IN2_L 
        self.PIN_IN2_R = PIN_IN2_R
        self.PIN_VREF_L = PIN_VREF_L
        self.PIN_VREF_R = PIN_VREF_R
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_IN1_L,GPIO.OUT)
        GPIO.setup(self.PIN_IN2_L,GPIO.OUT)
        GPIO.setup(self.PIN_IN1_R,GPIO.OUT)
        GPIO.setup(self.PIN_IN2_R,GPIO.OUT)
        
        wp.wiringPiSetupGpio()
        wp.pinMode(self.PIN_VREF_L, wp.GPIO.PWM_OUTPUT)
        wp.pinMode(self.PIN_VREF_R, wp.GPIO.PWM_OUTPUT)
        wp.pwmSetMode(wp.PWM_MODE_MS)
        wp.pwmSetRange(Drive.MaxdutyRange)
        wp.pwmSetClock(400) 
    
    def _drive_ad_R(self):
        GPIO.output(self.PIN_IN1_R,GPIO.HIGH)
        GPIO.output(self.PIN_IN2_R,GPIO.LOW)
        
    def _drive_ad_L(self):
        GPIO.output(self.PIN_IN1_L,GPIO.HIGH)
        GPIO.output(self.PIN_IN2_L,GPIO.LOW)
    
    def _drive_rev_R(self):
        GPIO.output(self.PIN_IN1_R,GPIO.LOW)
        GPIO.output(self.PIN_IN2_R,GPIO.HIGH)
        
    def _drive_rev_L(self):
        GPIO.output(self.PIN_IN1_L,GPIO.LOW)
        GPIO.output(self.PIN_IN2_L,GPIO.HIGH)
        
    def _brake_R(self):
        GPIO.output(self.PIN_IN1_R,GPIO.HIGH)
        GPIO.output(self.PIN_IN2_R,GPIO.HIGH)
        
    def _brake_L(self):
        GPIO.output(self.PIN_IN1_L,GPIO.HIGH)
        GPIO.output(self.PIN_IN2_L,GPIO.HIGH)
        
    def _stop_R(self):
        GPIO.output(self.PIN_IN1_R,GPIO.LOW)
        GPIO.output(self.PIN_IN2_R,GPIO.LOW)
        
    def _stop_L(self):
        GPIO.output(self.PIN_IN1_L,GPIO.LOW)
        GPIO.output(self.PIN_IN2_L,GPIO.LOW)
        
    def straight(self, duty, movetime):
        duty = int(Drive.MaxdutyRange*duty)
        wp.pwmWrite(self.PIN_VREF_R, duty)
        wp.pwmWrite(self.PIN_VREF_L, duty)
        self._drive_ad_R()
        self._drive_ad_L()
        time.sleep(movetime)
        
    def back(self, duty, movetime):
        duty = int(Drive.MaxdutyRange*duty)
        wp.pwmWrite(self.PIN_VREF_R, duty)
        wp.pwmWrite(self.PIN_VREF_L, duty)
        self._drive_rev_R()
        self._drive_rev_L()
        time.sleep(movetime)
        
    def turn_right(self, duty, movetime):
        duty = int(Drive.MaxdutyRange*duty)
        wp.pwmWrite(self.PIN_VREF_R, 0)
        wp.pwmWrite(self.PIN_VREF_L, duty)
        self._drive_ad_R()
        self._drive_ad_L()
        time.sleep(movetime)
        
    def turn_left(self, duty, movetime):
        duty = int(Drive.MaxdutyRange*duty)
        wp.pwmWrite(self.PIN_VREF_R, duty)
        wp.pwmWrite(self.PIN_VREF_L, 0)
        self._drive_ad_R()
        self._drive_ad_L()
        time.sleep(movetime)
        
    def Brake(self, movetime):
        self._brake_R()
        self._brake_L()
        time.sleep(movetime)
        
    def Stop(self, movetime):
        self._stop_R()
        self._stop_L()
        time.sleep(movetime)
        
if __name__ == '__main__':
    motor = Drive()
    motor.straight(0.4, 5)
    motor.Brake(0.01)
    motor.back(0.4, 5)
    motor.Brake(2)
    motor.back(0.6, 5)
    motor.Stop(2)
