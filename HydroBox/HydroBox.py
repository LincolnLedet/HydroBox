#test
import datetime
import time
from RPi import GPIO
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

#main
def main():
    lcd.cursor_pos = (0, 3)
    lcd.write_string('p')
    time.sleep(1);
    lcd.cursor_pos = (0, 6)
    smiley = (
    0b00000,
    0b01010,
    0b01010,
    0b00000,
    0b10001,
    0b10001,
    0b01110,
    0b00000)
    lcd.create_char(0, smiley)
    lcd.write_string('\x03')

    
main()