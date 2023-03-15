import datetime
from RPLCD import CharLCD
from RPi import GPIO
GPIO.setwarnings(False)
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])#defines LCD
import Adafruit_DHT
import time
mode = GPIO.getmode()
print (mode)


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
GPIO.setup(11,GPIO.OUT)
GPIO.output(11, GPIO.HIGH)

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)#makes sensor
    
    current_time = datetime.datetime.today()#gets clock
    hour = current_time.hour
    minute = current_time.minute
    if hour>12:
        hour= hour-12
        minute= (str(minute)+"pm")
    else:
        minute= (str(minute)+"am")
        
    if humidity is not None and temperature is not None:
        temperature = (float(temperature) * 9/5) + 32
        lcd.clear()
        if current_time.minute<10:
            lcd.write_string(str(hour)+":0"+str(minute))
        else:
            lcd.write_string(str(hour)+":"+str(minute))
        lcd.write_string("            ")
        lcd.write_string(str(temperature)+"F "+ str(humidity)+"%")
    else:
        print("")
    GPIO.output(11, GPIO.HIGH)
    time.sleep(.5);
    GPIO.output(11, GPIO.LOW)