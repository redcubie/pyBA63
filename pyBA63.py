#
# ---------- Main pyBA63 library ---------
#

import const # Import constant sendables
import serial # Import (py)serial

ser = serial.Serial() # Make Serial object

def open(port):
	ser.port = port # Ser serial port
	ser.parity = serial.PARITY_ODD # Set ODD parity
	ser.open() # Open serial port

def close():
	ser.close() # Close serial port

def SetCountryCode(number):
	value = bytearray([27, 82, number]) #\x1B\x52 number - Set Country Code
	ser.write(value) # Write value to serial

def SetCursor(x, y):
	value = bytearray([27, 91, y, 59, x, 72]) #\x1B\x5B y \x3B x \x48 - Set Cursor Position
	ser.write(value) # Write value to serial

def WriteData(data):
	length = len(data) # Get length of data
	value = bytearray([2, 0, length])+data.encode('ascii') #\x02\x00 length data - Format data for sending
	ser.write(value) # Write value to serial

def clear():
	ser.write(const.CLR) # Write clear to serial
	SetCursor(0, 0) # Set cursor to beginning