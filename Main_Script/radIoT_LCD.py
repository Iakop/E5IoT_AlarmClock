#!/usr/bin/python

# For time delays, and sleeping
import time

# For driving an LCD to display results.
import Adafruit_CharLCD as LCD

# Raspberry Pi LCD pin configuration:
lcd_rs        = 25
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 27
lcd_d7        = 22
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)
lcd.show_cursor(False)
lcd.clear()