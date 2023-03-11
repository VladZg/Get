#  import GPiO as

dac = []    # list of GPIO-pins from DAC

#
# GPIO.setmode
#
#

def Dec2Bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]

while True:
    try:
        while True:
            num = input("Type a number from 0 to 255: ")
            if 0 <= int(num) <= 255:
                print(Dec2Bin(int(num)))
            else:
                print("Number is out of range [0,255]!")
    except:
        if num == "q":
            break
        print("Not an integer!")

# GPIO.cleanup()
#
#
print("EOP")
