from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574',0x27) #I2C Adapter model
lcd.write_string('Hello') # Hello print
lcd.crlf() # 1 line space
lcd.write_string('World')
