#!/usr/bin/env python3
import serial
import json
import os

if __name__ == '__main__':
  nanoSerial = os.getenv('NANO_SERIAL', '/dev/ttyUSB0')
  baud = os.getenv('NANO_BAUD', 9600)
  ser = serial.Serial(nanoSerial, baud, timeout=1)
  ser.flush()
  while True:
    if ser.in_waiting > 0:
      response = ser.readline().decode('utf-8').rstrip()
      parse = json.loads(response)
      print(parse["humidity_percentage"])
      print(parse["temperature_celsius"])
      print(parse["temperature_fahrenheit"])
      print(parse["heat_index_celsius"])
      print(parse["heat_index_fhrenheit"])