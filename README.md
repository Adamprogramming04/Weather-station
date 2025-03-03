# Micro:bit Weather Station

This  micro:bit project uses the BBC micro:bit's built-in sensors to create a simple weather station that reads the temperature and light level. The temperature is measured in Celsius, and the light level is measured based on the ambient light received by the micro:bit's LED matrix.

## Features:
- **Temperature**: The micro:bit's built-in temperature sensor is used to measure the temperature in Celsius.
- **Light Level**: The light sensor detects the ambient light using the LED matrix's brightness.
- **Warnings**: If the temperature is too high (above 30°C) or too low (below 10°C), a warning is displayed on the micro:bit.
- **Serial Monitor Output**: Temperature and light level data is also printed to the serial monitor for further analysis.

## Instructions:
1. The micro:bit will display the current temperature on its LED screen.
2. It will also show the current light level by displaying a number.
3. If the temperature goes above 30°C or below 10°C, a warning will appear on the display (a sad face and "High Temp!" or "Low Temp!").
4. The serial monitor will display the data for further logging or analysis.

## Requirements:
- BBC micro:bit
- MicroPython installed
- USB connection to view serial output (for logging)

## How to Use:
1. Upload the code to your micro:bit using the Mu editor or any compatible MicroPython IDE.
2. Open the serial monitor (or use the REPL in Mu) to view the printed temperature and light level data.
3. Watch the micro:bit's LED matrix to see the data displayed.
4. The system will update every 2 seconds.

## Thresholds:
- If the temperature exceeds **30°C**, a warning is shown on the micro:bit.
- If the temperature drops below **10°C**, another warning will be shown.

