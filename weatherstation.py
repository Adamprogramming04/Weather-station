from microbit import *
import utime

# Thresholds for warning
HIGH_TEMP_THRESHOLD = 30  # Temperature above 30C
LOW_TEMP_THRESHOLD = 10   # Temperature below 10C

# Function to display the temperature and light levels on the LED screen
def display_data(temp, light_level):
    display.scroll("Temp: " + str(temp) + "C", wait=True)
    display.show(str(light_level))

# Function to display a warning if the temperature is too high or too low
def check_temperature(temp):
    if temp > HIGH_TEMP_THRESHOLD:
        display.show(Image.SAD)
        sleep(2000)
        display.clear()
        display.scroll("High Temp!", wait=True)
    elif temp < LOW_TEMP_THRESHOLD:
        display.show(Image.SAD)
        sleep(2000)
        display.clear()
        display.scroll("Low Temp!", wait=True)

# Main loop
while True:
    # Read temperature in Celsius
    temperature = temperature()
    
    # Read light level (range from 0 to 255)
    light_level = display.read_light_level()
    
    # Display temperature and light data on the LED screen
    display_data(temperature, light_level)
    
    # Check for high/low temperature warnings
    check_temperature(temperature)
    
    # Output data to serial monitor for logging
    print("Temperature: {}C, Light Level: {}".format(temperature, light_level))
    
    # Wait for a short time before taking another reading
    sleep(2000)  # Delay for 2 seconds
