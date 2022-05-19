import serial
import time

ser = serial.Serial('COM6',9600)
time.sleep(2)
ser.close()
ser.open()
time.sleep(2)

def getData():
    switchList = []
    a = "2"
    ser.write(a.encode())
    for i in range(10):
        read = ser.readline()
        data = read.decode()
        data = int(data.strip('\r\n'))
        print(data)
        switchList.append(data)
    sumList = sum(switchList)
    return sumList

def getDataShort():
    switchList = []
    ser.write(b'y')
    for i in range(5):
        read = ser.readline()
        data = read.decode()
        data = int(data.strip('\r\n'))
        print(data)
        switchList.append(data)
    sumList = sum(switchList)
    return sumList

def countDown():
    print('The exercise will begin in 3 seconds:')
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print('Exercise starting NOW!')

def getAlphabet(x):
    char = 'A'
    if x == 1:
        char = 'B'
    elif x == 2:
        char = 'C'
    elif x == 3:
        char = 'D'
    elif x == 4:
        char = 'E'
    elif x == 5:
        char = 'F'
    elif x == 6:
        char = 'G'
    elif x == 7:
        char = 'H'
    elif x == 8:
        char = 'I'
    elif x == 9:
        char = 'J'
    return char

def place():
    print("Now it's your turn.")
    time.sleep(1)
    print('Please enter your placement buy doing biceps!')
    countDown()
    letter = getAlphabet(getData())
    print('The letter you chose was ', letter, ". Now it's time to enter the number")
    number = str(getData())
    print('The number you chose was', number)
    placement = letter + number
    return placement


print(getDataShort())


