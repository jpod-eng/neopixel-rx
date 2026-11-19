let dist = 0
let color = 0
let brightness = 100
let strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
wuKong.lightIntensity(100)
wuKong.setLightMode(wuKong.LightMode.BREATH)
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    color = receivedNumber
})
basic.forever(function on_forever() {
    
    
    dist = sonarbit.sonarbit_distance(Distance_Unit.Distance_Unit_cm, DigitalPin.P1)
    strip.showColor(neopixel.hsl(color, 100, 10))
    // led.plot_bar_graph(dist, 400)
    basic.showNumber(dist)
})
