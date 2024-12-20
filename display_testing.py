import RPi.GPIO as GPIO
import spidev
import time

DC_PIN = 22
RST_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([DC_PIN, RST_PIN], GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 2000000
spi.mode = 0

def command(cmd):
    GPIO.output(DC_PIN, GPIO.LOW)
    spi.xfer([cmd])

def data(d):
    GPIO.output(DC_PIN, GPIO.HIGH)
    spi.xfer([d])

try:
    GPIO.output(RST_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(RST_PIN, GPIO.HIGH)
    time.sleep(0.1)

    command(0x11)  # Sleep out
    time.sleep(0.2)
    command(0x29)  # Display on
    
    # Fill red - only try once
    command(0x2C)
    pixels_sent = 0
    total_pixels = 240 * 240
    while pixels_sent < total_pixels:
        data(0xFF)
        data(0x00)
        data(0x00)
        pixels_sent += 1
        if pixels_sent % 1000 == 0:
            print(f"Sent {pixels_sent}/{total_pixels} pixels")

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    spi.close()