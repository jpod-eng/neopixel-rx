
dist = 0
color = 0
brightness = 100
strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
wuKong.light_intensity(100)
wuKong.set_light_mode(wuKong.LightMode.BREATH)

def on_received_number(receivedNumber):
    global color
    color = receivedNumber

radio.on_received_number(on_received_number)

def on_forever():
    global brightness
    global dist
    dist = sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_CM, DigitalPin.P1)
    strip.show_color(neopixel.hsl(color, 100, 10))
    #led.plot_bar_graph(dist, 400)

    basic.show_number(dist)

basic.forever(on_forever)

