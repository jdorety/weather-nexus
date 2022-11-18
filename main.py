from dotenv import load_dotenv
import time
from os import environ
from helpers import make_tx, send_readings
import board
from adafruit_bme280 import basic as adafruit_bme280

load_dotenv()
key = environ.get('api-key')
ledger_url = environ.get('ledger-url')

i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

bme280.sea_level_pressure = 1022

print("\nTemperature: %0.1f C" % bme280.temperature)
print("Humidity: %0.1f %%" % bme280.humidity)
print("Pressure: %0.1f hPa" % bme280.pressure)
print("Altitude = %0.2f meters" % bme280.altitude)

while True:
  temp = bme280.temperature
  hum = bme280.humidity
  pres = bme280.pressure

  tx = make_tx(temp, pres, hum)
  response = send_readings(ledger_url, key, tx)
  time.sleep(10)



# print(response)