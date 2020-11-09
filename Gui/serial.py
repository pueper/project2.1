import serial

ser = serial.Serial('COM3', 19200)

while True:
    line = ser.readline()
    #data voor licht
    #def licht_data():
        #for(licht in line):
            #c = licht

    #data voor temperatuur
    #def temperatuur_data():
        #for(temperatuur in line):
            #b = temperatuur

    #lengte zonnescherm
    #def lengte_zonnescherm():
        #for(lengte in data):
            #a = lengte zonnescherm

