import RPi.GPIO as io
import time

io.setmode(io.BOARD)
io.setup(3, io.OUT)
io.setup(5, io.OUT)
io.setup(7, io.OUT)
io.setup(11, io.OUT)
io.setup(13, io.OUT)
io.setup(15, io.OUT)
io.setup(19, io.OUT)
io.setup(21, io.OUT)

def decimalToBinary(num):
  binary = bin(num)[2:]
  return binary

If __name__ == ‘__main__’
  dec = int(input(‘Enter Decimal: ‘’))
  binaryString = decimalToBinary(dec)
  binaryArray = list(binaryString)

while(1):
  If binaryArray[0] == ‘1’:
    io.output(3, io.HIGH)
    time.sleep(0.5)
  else:
    io.output(3, io.LOW)
    time.sleep(0.5)
  If binaryArray[1] == ‘1’:
    io.output(5, io.HIGH)
    time.sleep(0.5)
  else:
    io.output(5, io.LOW)
    time.sleep(0.5)
  If binaryArray[2] == ‘1’:
    io.output(7, io.HIGH)
    time.sleep(0.5)
  else:
    io.output(7, io.LOW)
    time.sleep(0.5)
  If binaryArray[3] == ‘1’:
    io.output(11, io.HIGH)
    time.sleep(0.5)
  else:
    io.output(11, io.LOW)
    time.sleep(0.5)
  If binaryArray[4] == ‘1’:
    io.output(13, io.HIGH)
    time.sleep(0.5)
  else:
    io.output(13, io.LOW)
    time.sleep(0.5)
  If binaryArray[5] == ‘1’:
    io.output(15, io.HIGH)
    time.sleep(0.5)
  else:
    io.output(15, io.LOW)
    time.sleep(0.5)
  If binaryArray[6] == ‘1’:
    io.output(19, io.HIGH)
    time.sleep(0.5)
  else:
    io.output(19, io.LOW)
    time.sleep(0.5)
  If binaryArray[7] == ‘1’:
    io.output(21, io.HIGH)
    time.sleep(0.5)
  else:
    io.output(21, io.LOW)
    time.sleep(0.5)

io.cleanup()
