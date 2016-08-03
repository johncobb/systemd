import threading
import time
import Queue
import subprocess
import wiringpi as GPIO


class CpGpioMap():
    GPIO_CELLENABLE = 17
    GPIO_CELLRESET = 6
    GPIO_CELLONOFF = 5
    GPIO_CELLPWRMON = 26
    GPIO_LED1 = 23
    GPIO_LED2 = 24
    

            

# !!! This method must be called before creating the modem object !!!
def led_init():

    

    print 'Initializing Led(s)'

    GPIO.pinMode(CpGpioMap.GPIO_LED1, GPIO.OUTPUT) #LED1
    GPIO.pinMode(CpGpioMap.GPIO_LED2, GPIO.OUTPUT) #LED2

    print 'Led(s) Initialized' 

        
if __name__ == '__main__':
    
    
    GPIO.wiringPiSetupGpio()

    led_init()
    
    while True:
        GPIO.digitalWrite(CpGpioMap.GPIO_LED1, GPIO.GPIO.HIGH)
        GPIO.digitalWrite(CpGpioMap.GPIO_LED2, GPIO.GPIO.LOW)
        time.sleep(.25)
        GPIO.digitalWrite(CpGpioMap.GPIO_LED1, GPIO.GPIO.LOW)
        GPIO.digitalWrite(CpGpioMap.GPIO_LED2, GPIO.GPIO.HIGH)
        time.sleep(.25)
        

    print 'Exiting App...'
    exit()
