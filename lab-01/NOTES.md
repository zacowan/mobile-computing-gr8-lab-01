# Notes

## Meeting 1

- Use ultrasonic sensor to actuate a light bulb color based on distance

### OHM's Law

V = IR

I is in A, V is in V, R is in Ohms

### To-Do

- Make video
  - Group 8, names, SSH connections, sensor + actuator connections
- Write code for ultrasonic sensor to LED
- Report

### Sensor

- Range: 2cm -> 400cm (~13ft) at 5v (~15 degree angle of measurement)
- VCC -> Pin 2
- GND -> Pin 6
- TRIG -> Pin 12 (GPIO18)
- ECHO -> 300ohm resistor -> Pin 18 (GPIO24)
- ECHO -> 470ohm resistor -> Pin 6 (GND)

### LEDs

- 330ohm resistor
