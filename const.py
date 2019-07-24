#
# ---------- CONSTANTS FOR pyBA63 ----------
#

LF = bytearray([10]) #\x0A - Line Feed
CR = bytearray([13]) #\x0D - Carriage Return
CLR = bytearray([27, 91, 50, 74]) #\x1B\x5B\x32\x4A - Clear Display
DEL = bytearray([27, 91, 48, 75]) #\x1B\x5B\x30\x4B - Delete to End of Line
BS = bytearray([8]) #\x08 - Backspace without deleting