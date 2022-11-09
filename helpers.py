from requests import post

def make_tx(temperature, pressure, moisture):
  now = "#(now)"
  temp = {
    "_id": "temperature",
    "reading": temperature,
    "recordedAt": now
  }
  press = {
    "_id": "pressure",
    "reading": pressure,
    "recordedAt": now
  }
  moist = {
    "_id": "moisture",
    "reading": moisture,
    "recordedAt": now
  }
  return [temp, press, moist]

def send_readings(path, key, data):
  operation = "transact"
  url = f'{path}{operation}'
  headers = {
  "Authorization": f'Bearer {key}'
}

  r = post(url, json=data, headers=headers)
  return r.json()