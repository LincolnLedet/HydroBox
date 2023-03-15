#test
import datetime
from RPi import GPIO
from RPLCD.gpio import CharLCD
GPIO.setwarnings(False)


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
lcd.write_string('Hello world')
sleep(33)

def main():
    
    #LCD STUff
    # Main program block

    
    lcd.write_string('Hello world')
    sleep(33)
