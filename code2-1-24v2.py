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

# Main animation loop
while True:
    color_wipe((255, 0, 0), 0.1)  # Red wipe
    time.sleep(0.5)
    color_wipe((0, 255, 0), 0.1)  # Green wipe
    time.sleep(0.5)
    color_wipe((0, 0, 255), 0.1)  # Blue wipe
    time.sleep(0.5)
