import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

def color_wipe(color, wait):
    for i in range(len(pixels)):
        pixels[i] = color
    pixels.show()
    time.sleep(wait)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(len(pixels)):
            pixel_index = (i * 256 // len(pixels)) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def wheel(pos):
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

while True:
    # Animation 1: Red, Green, Blue wipe
    color_wipe((255, 0, 0), 0.1)
    time.sleep(0.5)
    color_wipe((0, 255, 0), 0.1)
    time.sleep(0.5)
    color_wipe((0, 0, 255), 0.1)
    time.sleep(0.5)

    # Animation 2: White blink
    pixels.fill((255, 255, 255))
    pixels.show()
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(0.5)

    # Animation 3: Rainbow cycle
    rainbow_cycle(0.1)

    # Animation 4: Custom pattern
    for i in range(len(pixels)):
        pixels[i] = (255, 0, 255)  # Magenta
    pixels.show()
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
