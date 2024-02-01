import time
import board
import neopixel

# Define the number of NeoPixels on Circuit Playground
num_pixels = 10
pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=0.2, auto_write=False)

def color_wipe(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        pixels.show()
        time.sleep(wait)

# Define RGB color values
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Main animation loop
while True:
    color_wipe(red, 0.1)     # Red wipe
    color_wipe(green, 0.1)   # Green wipe
    color_wipe(blue, 0.1)    # Blue wipe
