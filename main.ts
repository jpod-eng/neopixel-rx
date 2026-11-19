radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    color = receivedNumber
})
let color = 0
let brightness = 100
let strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
wuKong.lightIntensity(100)
wuKong.setLightMode(wuKong.LightMode.BREATH)
basic.forever(function on_forever() {
    
    brightness = 50
    strip.showColor(neopixel.hsl(color, 100, brightness))
})
