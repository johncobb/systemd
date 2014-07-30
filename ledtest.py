import threading
import time
import Queue
import subprocess
import Adafruit_BBIO.UART as UART
import Adafruit_BBIO.GPIO as GPIO

class CpGpioMap():
    GPIO_CELLENABLE = "P9_12"
    GPIO_CELLRESET = "P9_23"
    GPIO_CELLONOFF = "P8_12"
    GPIO_CELLPWRMON = "P9_42"
    GPIO_LED1 = "P8_14"
    GPIO_LED2 = "P8_15"
    

            

# !!! This method must be called before creating the modem object !!!
def led_init():

    

    print 'Initializing Led(s)'

    GPIO.setup(CpGpioMap.GPIO_LED1, GPIO.OUT) #LED1
    GPIO.setup(CpGpioMap.GPIO_LED2, GPIO.OUT) #LED2

    print 'Led(s) Initialized' 

        
if __name__ == '__main__':
    
    
    led_init()
    
    while True:
        GPIO.output(CpGpioMap.GPIO_LED1, GPIO.HIGH)
        GPIO.output(CpGpioMap.GPIO_LED2, GPIO.LOW)
        time.sleep(.25)
        GPIO.output(CpGpioMap.GPIO_LED1, GPIO.LOW)
        GPIO.output(CpGpioMap.GPIO_LED2, GPIO.HIGH)
        time.sleep(.25)
        

    print 'Exiting App...'
    exit()