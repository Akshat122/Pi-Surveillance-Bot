import RPi.GPIO as GPIO
import urllib2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
#true = 1
#while(true):
                #try:
   # response1 = urllib2.urlopen('http://192.168.177.1/buttonStatus1.txt')
    #status1 = response1.read()
   # response2 = urllib2.urlopen('http://192.168.177.1/buttonStatus2.txt')
  #  status2 = response2.read()
   # response3 = urllib2.urlopen('http://192.168.177.1/xampp/buttonStatus3.txt')
    #status3 = response3.read()
    #response4 = urllib2.urlopen('http://192.168.177.1/xampp/buttonStatus4.txt')
    #status4 = response4.read()
                        
               # except urllib2.HTTPError, e:
                  #                      print e.code

        #        except urllib2.URLError, e:
             #                           print e.args


   # if status1=='forward':
         GPIO.output(7,True)
        # print status1
    #if status1=='OFF':
     #    GPIO.output(32,True)
      #   print status1
    #if status2=='ON':
     #   GPIO.output(26,False)
#    if status2=='OFF':
 #       GPIO.output(26,True)
  #  if status3=='ON':
   #     GPIO.output(24,False)
    #if status3=='OFF':
     #   GPIO.output(24,True)
#    if status4=='ON':
  #      GPIO.output(22,False)
 #   if status4=='OFF':
   #     GPIO.output(22,True)
 
                

