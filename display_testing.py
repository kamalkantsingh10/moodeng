#!/usr/bin/python3

from luma.lcd.device import st7789
from luma.core.interface.serial import spi
from luma.core.render import canvas
from PIL import ImageFont
import time

# Pin Definitions (BCM numbering)
# ============================================
# Change these numbers according to your wiring
RST_PIN = 4    # Reset pin
DC_PIN = 27     # Data/Command pin (sometimes labeled as CD)
CS_PIN = 8      # Chip Select pin
BL_PIN = 22     # Backlight pin (if your display has it)

# Note: Other pins that must be connected but don't need GPIO numbers:
# SDA/MOSI -> Connect to MOSI (GPIO 10)
# SCL/SCK  -> Connect to SCLK (GPIO 11)
# VCC      -> Connect to 3.3V
# GND      -> Connect to Ground

def init_display():
    # Initialize SPI interface
    serial = spi(
        port=0,           # SPI port 0
        device=0,         # CE0 (use 1 for CE1)
        gpio_DC=DC_PIN,   # Data/Command pin
        gpio_RST=RST_PIN, # Reset pin
        bus_speed_hz=32000000
    )
    
    # Initialize the display device
    device = st7789(
        serial,
        width=280,        # Display width
        height=240,       # Display height
        rotate=1          # Rotation (0, 1, 2, 3) each represents 90 degree rotation
    )
    
    return device

def main():
    print("Initializing display...")
    device = init_display()
    
    # Try to load a font, fall back to default if not found
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except:
        font = ImageFont.load_default()
    
    print("Starting demo...")
    
    while True:
        # Draw frame
        with canvas(device) as draw:
            # Draw a border
            draw.rectangle(device.bounding_box, outline="white")
            
            # Draw some shapes
            draw.rectangle((40, 40, 100, 100), fill="red")
            draw.ellipse((120, 40, 180, 100), fill="blue")
            draw.polygon([(200, 40), (260, 100), (200, 100)], fill="green")
            
            # Add text
            draw.text((40, 120), "ST7789 Demo", fill="white", font=font)
            draw.text((40, 150), f"CS={CS_PIN}, DC={DC_PIN}", fill="yellow", font=font)
            draw.text((40, 180), f"RST={RST_PIN}, BL={BL_PIN}", fill="yellow", font=font)
        
        # Wait for 2 seconds
        time.sleep(2)





main()