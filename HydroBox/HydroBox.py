#test
import datetime
import time
from RPi import GPIO
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
GPIO.setwarnings(False)

#LCD init
LCD_RS = 15
LCD_E  = 13
LCD_D4 = 11
LCD_D5 = 7
LCD_D6 = 5
LCD_D7 = 3
lcd = CharLCD(pin_rs=LCD_RS, pin_rw=8, pin_e=LCD_E, pins_data=[LCD_D4, LCD_D5, LCD_D6, LCD_D7],
              numbering_mode=GPIO.BOARD,
             cols=16, rows=2, dotsize=8,
             charmap='A02',
             auto_linebreaks=True)
#fan init
fan = 19
GPIO.setup(fan, GPIO.OUT)


#main
def main():
    #boot up
    lcd.clear()
    time.sleep(1)
    lcd.cursor_pos = (0, 0)
    time.sleep(.1)
    lcd.write_string('   Welcome to ')
    lcd.cursor_pos = (1, 0)
    lcd.write_string('    HydroBox!')
    time.sleep(1)
    GPIO.output(fan, GPIO.HIGH)
    time.sleep(80)
    GPIO.output(fan, GPIO.LOW)
    time.sleep(.1)
    GPIO.output(fan, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(fan, GPIO.LOW)
    lcd.clear()
    
    #Temp
    #Light Time
    #Fans
#def displayTemp()

#def displayLightTimes()

#def Fans()
    
main()