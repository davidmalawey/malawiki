---
type: entity
kind: tool
aliases: ["NodeMCU", "ESP8266", "ESP"]
first_seen: "[[videos/program-a-plc-with-conveyor-arduino-and-industrial-robot]]"
tags: [microcontroller, wifi, sensor-node]
source_count: 3
---

# ESP8266 / NodeMCU

Wi-Fi-capable microcontroller board used in the MXET conveyor demo as a sensor node — reads the [[entities/tools/vl53-distance-sensor|VL53]] over I2C and signals the [[entities/tools/p1am-100|PLC]] via a digital GPIO line.

## Appears in

- [[videos/program-a-plc-with-conveyor-arduino-and-industrial-robot]]
- [[videos/iot-using-mqtt-on-esp8266-set-your-client-id-or-autogenerate-credentials]]
- [[videos/scuttle-robot-iot-in-all-forms-esp-pc-mobile-phone-raspi-demo-with-buzzer]]

## Related

- [[entities/tools/vl53-distance-sensor]]
- [[concepts/i2c-sensor-integration]]
