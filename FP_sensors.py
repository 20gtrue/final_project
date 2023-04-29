import time
import RPi.GPIO as GPIO

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

GPIO.setmode(GPIO.BCM) # Use BCM Configuration
GPIO.setwarnings(False)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Set channels as outputs
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT) # Set LED as an Output; BCM 17

while True:
  print("READING DATA....")
  
  GPIO.output(led_pin, GPIO.HIGH)   # Turn on LED Before Reading Sound
  time.sleep(0.5)
  sound_sum = 0   # Reset sound sum to 0
  sound_channel = 1   # Sound sensor on channel 0
  for i in range(50):
    sound_val = mcp.read_adc(sound_channel)   # Read Sound Sensor on Channel 0
    print("Value: " + str(sound_val))
    sound_sum = sound_sum + sound_val
    time.sleep(0.1)
  sound_avg = sound_sum/50
  print("Average Value: " + str(sound_avg))
  GPIO.output(led_pin, GPIO.LOW)
  print("NOT READING DATA....")
  
  # PUBLISHER CODE HERE
  
  time.sleep(15) 
