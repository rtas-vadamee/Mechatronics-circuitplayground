import time
import board
import neopixel

# Define the onboard NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

try:
    while True:
        # Blink in red
        pixels.fill((255, 0, 0))
        pixels.show()
        time.sleep(0.5)

        # Blink in blue
        pixels.fill((0, 0, 255))
        pixels.show()
        time.sleep(0.5)

except KeyboardInterrupt:
    # Turn off NeoPixels before exiting
    pixels.fill((0, 0, 0))
    pixels.show()
