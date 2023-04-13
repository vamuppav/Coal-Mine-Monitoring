import RPi.GPIO as GPIO
import serial
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)

import urllib.request as urllib2
port=serial.Serial("/dev/ttyAMA0", baudrate=9600,timeout=1.0)
myAPI = "Z0NG72JCVLG8EZGV"
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI # THINGSPEAK
print(baseURL)
while True:
    rcv=port.read(9)
    print(rcv)
    x=(rcv[0:2])
    y=(rcv[2:4])
    z=(rcv[4:5])
    w=(rcv[5:7])
    o=(rcv[7:])
    water=int(o)
    print(water)
    
    
    print ("--------------------------------------------")
    data = ("temperature: {} ".format( x)) + ("humidity: {} ".format(y)) + ("heart beat: {} ".format(z))+("smoke: {} ".format(o))
    print(data)
    urllib2.urlopen(((baseURL +"&field1=%s" % (str(x))))+(baseURL +"&field2=%s" % (str(y)))+(baseURL +"&field3=%s" % (str(z)))+(baseURL +"&field4=%s" % (str(o))))
    
    

