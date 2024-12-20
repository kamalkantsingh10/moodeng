from robot_hat import Pin,TTS,Servo, PWM
from robot_hat.utils import get_battery_voltage
import time


pin = Pin("LED")
tts=TTS(lang='en-GB')
pin1 = PWM("P0")
tail_base = Servo(channel= 0)                      # set the servo angle

ms_del =50
for i in range(1,25):
    tail_base.angle(0)
    time.sleep(0.3)
    tail_base.angle(-10)
    time.sleep(0.3)
    tail_base.angle(0)
    time.sleep(0.3)
    tail_base.angle(10)
    time.sleep(0.3)

    print(str(i) + "    battery: "+str(get_battery_voltage()))


# for i in range (1,25):
#     tail_base2.angle(-30)
#     time.sleep(ms_del/1000)
#     tail_base1.angle(70)
#     time.sleep(0.3)
#     tail_base.angle(30)
#     time.sleep(0.3)
#     tail_base2.angle(30)
#     time.sleep(ms_del/1000)
#     tail_base1.angle(-50)
#     time.sleep(0.3)
#     tail_base.angle(-70)
#     time.sleep(0.3)
#     print(str(i) + "    battery: "+str(get_battery_voltage()))



tail_base.angle(0)