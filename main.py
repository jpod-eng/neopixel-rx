def on_received_number(receivedNumber):
    global color
    color = receivedNumber
radio.on_received_number(on_received_number)

color = 0
brightness = 100
strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
wuKong.light_intensity(100)
wuKong.set_light_mode(wuKong.LightMode.BREATH)

def on_forever():
    global brightness
    brightness = 50
    strip.show_color(neopixel.hsl(color, 100, brightness))
basic.forever(on_forever)
