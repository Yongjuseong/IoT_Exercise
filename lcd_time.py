from RPLCD.i2c import CharLCD
import time
import datetime # python date module
lcd = CharLCD('PCF8574',0x27)
try:
	while True:
		now = datetime.datetime.now() # current time
		nowDate = now.strftime('%Y-%m-%d') # today's date parsing
		nowTime = now.strftime('%H-%M:%S') # today's time parsing
		print(now,nowDate,nowTime)
		time.sleep(1)
		lcd.clear()
		lcd.cursor_pos = (0,3) # Position to mark letters
		lcd.write_string(nowDate)
		lcd.crlf()
		lcd.cursor_pos = (1,4)
		lcd.write_string(nowTime)

except KeyboardInterrupt:
	lcd.clear() # LCD clean

