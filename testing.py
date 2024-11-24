from robot_hat import Pin,TTS,Servo, PWM
import time


pin = Pin("LED")
tts=TTS(lang='en-GB')
pin1 = PWM("P0")
ser = Servo(channel=8)                      # set the servo angle
faceServo=Servo(channel=9)
faceServo1=Servo(channel=1)

faceServo2=Servo(channel=0)
ms_del =50

for i in range (1,25):
    pin.value(1)
    val = ser.angle(60)
    time.sleep(ms_del/1000)
    faceServo.angle(-60)
    time.sleep(ms_del/1000)
    faceServo1.angle(-60)
    time.sleep(ms_del/1000)
    faceServo2.angle(60)
    time.sleep(2)
    tts.say("doing the phase number " + str(i))
    pin.value(0)
    val = ser.angle(-60)
    time.sleep(ms_del/1000)
    faceServo2.angle(-60)
    time.sleep(ms_del/1000)
    faceServo.angle(60)
    time.sleep(ms_del/1000)
    faceServo1.angle(60)
    time.sleep(2)
    tts.say("I am done")
    print(i)

